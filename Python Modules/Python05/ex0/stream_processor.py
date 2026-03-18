#!/usr/bin/env python3


from typing import Any, List
from abc import ABC, abstractmethod


def count_words(text: str) -> int:
    words = 0
    for i in range(len(text)):
        if text[i] != " " and (i == 0 or text[i - 1] == " "):
            words += 1
    return words


class DataProcessor(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def process(self, data: Any) -> str:
        average = sum(data) / len(data)
        return (f"Processed {len(data)} numeric values,"
                f" sum={sum(data)}, avg={average:.1f}")

    def validate(self, data: Any) -> bool:
        try:
            for item in data:
                int(item)
            print("Validation: Numeric data verified")
            return True
        except (ValueError, TypeError):
            print("Error: Invalid numeric data")
            return False


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def process(self, data: Any) -> str:
        words = count_words(data)
        return f"Processed text: {len(data)} characters, {words} words"

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            print("Validation: Text data verified")
            return True
        else:
            print("Error: Invalid text data")
            return False


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def process(self, data: Any) -> str:
        if "INFO" in data:
            return "[INFO] INFO level detected: System ready"
        elif "ERROR" in data:
            return "[ALERT] ERROR level detected: Connection timeout"

    def validate(self, data: Any) -> bool:
        if isinstance(data, str) and ("ERROR" in data or "INFO" in data):
            print("Validation: Log entry verified")
            return True
        else:
            print("Error: Invalid log data")
            return False


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    print("\nInitializing Numeric Processor...")
    process_num = NumericProcessor()
    num_list: List = [1, 2, 3, 4, 5]
    if process_num.validate(num_list):
        result = process_num.process(num_list)
        print(process_num.format_output(result))

    print("\nInitializing Text Processor...")
    process_text = TextProcessor()
    text = "Hello Nexus World"
    if process_text.validate(text):
        result = process_text.process(text)
        print(process_text.format_output(result))

    print("\nInitializing Log Processor...")
    process_log = LogProcessor()
    log = "ERROR: Connection timeout"
    if process_log.validate(log):
        result = process_log.process(log)
        print(process_log.format_output(result))

    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")
    test_num = [1, 2, 3]
    test_str = "Hello World"
    test_log = "INFO: System ready"
    data_sample = [test_num, test_str, test_log]
    processors = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor()
    ]
    for i in range(len(processors)):
        processor = processors[i]
        data = data_sample[i]
        result = processor.process(data)
        print(f"Result {i+1}: {result}")

    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
