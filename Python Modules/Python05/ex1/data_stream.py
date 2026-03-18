#!/usr/bin/env python3


from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
        }


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            temperatures = self.filter_data(data_batch, "temperature")
            avg_temp = sum(temperatures) / len(temperatures)
        except (ValueError, TypeError, ZeroDivisionError):
            return "Error processing data"
        return (f"Sensor analysis: {len(data_batch)} readings processed,"
                f" avg temp: {avg_temp:.1f}°C")

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria == "temperature":
            result = [d["value"] for d in data_batch
                      if d["type"] == "temperature"]
        elif criteria == "humidity":
            result = [d["value"] for d in data_batch
                      if d["type"] == "humidity"]
        elif criteria == "pressure":
            result = [d["value"] for d in data_batch
                      if d["type"] == "pressure"]
        else:
            result = data_batch
        return result

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["type"] = "Environmental Data"
        return stats


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            sells = self.filter_data(data_batch, "sell")
            boughts = self.filter_data(data_batch, "buy")
            net_flow = sum(boughts) - sum(sells)
        except (ValueError, TypeError):
            return "Error processing data"
        return (f"Transaction analysis: {len(data_batch)}"
                f" operations, net flow: {net_flow} units")

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria == "sell":
            result = [d["value"] for d in data_batch if d["type"] == "sell"]
        elif criteria == "buy":
            result = [d["value"] for d in data_batch if d["type"] == "buy"]
        else:
            result = [d["value"] for d in data_batch]
        return result

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["type"] = "Financial Data"
        return stats


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        errors = self.filter_data(data_batch, "error")
        return (f"Event analysis: {len(data_batch)} events,"
                f" {len(errors)} error detected")

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria == "error":
            return [event for event in data_batch if event == "error"]
        else:
            return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["type"] = "System Events"
        return stats


class StreamProcessor:
    def __init__(self, streams: List[DataStream]) -> None:
        self.streams = streams

    def process_batches(self, batch: List[List[Any]]) -> List[str]:
        results = []
        for i in range(len(self.streams)):
            stream = self.streams[i]
            data = batch[i]
            result = stream.process_batch(data)
            results.append(result)
        return results


def filtering_demo() -> None:
    print("\nStream filtering active: High-priority data only")
    sensor_data = [
        {"type": "temperature", "value": 40},
        {"type": "temperature", "value": 36},
        {"type": "temperature", "value": 25},
        {"type": "humidity", "value": 65},
    ]
    trans_data = [
        {"type": "sell", "value": 750},
        {"type": "buy", "value": 150},
        {"type": "sell", "value": 450},
    ]
    sensor_stream = SensorStream("SENSOR_FILTER")
    trans_stream = TransactionStream("TRANS_FILTER")
    sensor = sensor_stream.filter_data(sensor_data, "temperature")
    trans = trans_stream.filter_data(trans_data, "sell")
    critical_alerts = [tmp for tmp in sensor if tmp > 35]
    high_trans = [t for t in trans if t > 500]
    print(f"Filtered results: {len(critical_alerts)}"
          f" critical sensor alerts, {len(high_trans)} large transaction")


def individual_stream_test() -> None:
    print("\nInitializing Sensor Stream...")
    data_batch = [
        {"type": "temperature", "value": 22.5},
        {"type": "humidity", "value": 60},
        {"type": "pressure", "value": 1013}
    ]
    sensor = SensorStream("SENSOR_001")
    stats = sensor.get_stats()
    print(f"Stream ID: {stats['stream_id']}, Type: {stats['type']}")
    items = ", ".join(f"{d['type']}:{d['value']}" for d in data_batch)
    print(f"Processing sensor batch:"
          f" [{items}]")
    print(f"{sensor.process_batch(data_batch)}")

    print("\nInitializing Transaction Stream...")
    data_batch = [
        {"type": "buy", "value": 100},
        {"type": "sell", "value": 150},
        {"type": "buy", "value": 75},
    ]
    trans = TransactionStream("TRANS_001")
    stats = trans.get_stats()
    print(f"Stream ID: {stats['stream_id']}, Type: {stats['type']}")
    items = ", ".join(f"{d['type']}:{d['value']}" for d in data_batch)
    print(f"Processing transaction batch:"
          f" [{items}]")
    print(f"{trans.process_batch(data_batch)}")

    print("\nInitializing Event Stream...")
    data_batch = ["login", "error", "logout"]
    event = EventStream("EVENT_001")
    stats = event.get_stats()
    print(f"Stream ID: {stats['stream_id']}, Type: {stats['type']}")
    print(f"Processing event batch:"
          f" [{', '.join(d for d in data_batch)}]")
    print(f"{event.process_batch(data_batch)}")


def polymorphic_test() -> None:
    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")
    streams = [
        SensorStream("SENSOR_002"),
        TransactionStream("TRANS_002"),
        EventStream("EVENT_002")
    ]
    processor = StreamProcessor(streams)
    sensor_data = [
        {"type": "temperature", "value": 25},
        {"type": "humidity", "value": 65},
    ]
    trans_data = [
        {"type": "sell", "value": 1000},
        {"type": "buy", "value": 150},
        {"type": "sell", "value": 450},
        {"type": "buy", "value": 65},
    ]
    event_data = ["login", "error", "logout"]
    batch1 = [sensor_data, trans_data, event_data]
    print("\nBatch 1 Results:")
    results = processor.process_batches(batch1)
    for r in results:
        print(f"- {r}")


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    individual_stream_test()
    polymorphic_test()
    filtering_demo()
    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
