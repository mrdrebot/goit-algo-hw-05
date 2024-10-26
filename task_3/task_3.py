import sys
from pathlib import Path
from collections import defaultdict

def parse_log_line(line: str) -> dict:
    keys_list = ["date", "time", "level", "message"]
    data_line_list: list = line.strip().split(" ", 3)
    line_dic: dict = dict(zip(keys_list, data_line_list))
    return line_dic

def filter_logs_by_level(logs: list, level: str) -> list:
    filer_logs_list: list = []
    
    if level != "":
        filer_logs_list = [log for log in logs if log['level'].lower() == level.lower()]
        print(f"\nDetails of the logs for the level '{level.upper()}':")
        
        for log in filer_logs_list:
            print(f"{log['date']} {log['time']} {log['level']} {log['message']}")
    else:
        filer_logs_list = logs
        
    return filer_logs_list

def count_logs_by_level(logs: list) -> dict:
    level_counter: dict = defaultdict(int)

    for log in logs:
        level_counter[log['level']] += 1
    
    return level_counter

def display_log_counts(counts: dict) -> None:
    first_block_width: int = 20
    second_block_width: int = 10
    separate_line: int = first_block_width + second_block_width

    print(f"\n{'Logging level':<{first_block_width}} | {'Number':<{second_block_width}}")
    print("-" * separate_line)

    for level, count in counts.items():
        print(f"{level:<{first_block_width}} | {count:<{second_block_width}}")
        

def load_logs(file_path: str) -> list:
    try:
        logs_list: list = []
        
        with open(file_path, 'r', encoding = 'utf-8') as file:
            logs_list = [parse_log_line(file_row) for file_row in file.readlines()]

            if not logs_list:
                raise ValueError("The find is empty!")
            
        return logs_list
    except FileNotFoundError:
        raise FileNotFoundError("The program could not find the file!")
    except Exception as e:
        raise Exception(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f'\nThe path to the file is not specified!\nCorrect command to run: python [<start file path>] [<directory path>] <logs level>')
    else:
        try:
            parse_logs_list: list = load_logs(Path(fr'{sys.argv[1]}'))
            counts_dict: dict = count_logs_by_level(parse_logs_list)
            log_level: str = sys.argv[2] if len(sys.argv) > 2 else ""
            value: bool = counts_dict.get(log_level.upper())

            if value == None and len(sys.argv) > 2:
                raise ValueError(f"The entered log level doesn`t exist! Change log level")

            display_log_counts(counts_dict)
            filter_logs_by_level(parse_logs_list, log_level)
        except Exception as e:
            print(f"Error: { e }")

