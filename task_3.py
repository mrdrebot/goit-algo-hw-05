import sys
from pathlib import Path
from collections import defaultdict

def parse_log_line(line: str) -> dict:
    keys_list = ["date", "time", "level", "massage"]
    data_line_list: list = line.strip().split(" ", 3)
    # print(data_line_list)
    line_dic: dict = dict(zip(keys_list, data_line_list))
    # print(line_dic)
    return line_dic



def filter_logs_by_level(logs: list, level: str) -> list:
    # print(f"level = {level.lower()}")
    # filtered_log_list = [log for log in logs if log['level'] == level]
    filtered_log_list = [log for log in logs if log['level'].lower() == level.lower()]
    #print(filtered_log_list)

    #for log in logs:
        # print(log)
       # print(log['level'].lower())
        #if log['level'] == level:
            # print(log)
            #filtered_log_list.append(log) 

    return filtered_log_list

def count_logs_by_level(logs: list) -> dict:
    level_counter = defaultdict(int)

    for log in logs:
        level_counter[log['level']] += 1
        #print(log)
    
    #print(level_counter)
    return level_counter

def display_log_counts(counts: dict) -> None:
    first_block_width = 20
    second_block_width = 10
    separate_line = first_block_width + second_block_width + 3

    print(f"\n{'Рівень логування':<{first_block_width}} | {'Кількість':<{second_block_width}}")
    print("-" * separate_line)

    for level, count in counts.items():
        print(f"{level:<{first_block_width}} | {count:<{second_block_width}}")

def load_logs(file_path: str) -> list:
    try:
        parse_log_list: list = []
        log_level = sys.argv[2] if len(sys.argv) > 2 else ""
        with open(file_path, 'r', encoding = 'utf-8') as file:
            for el in file.readlines():
                # print(el)
                parse_log_list.append(parse_log_line(el))
            # print(parse_log_list)
        filter_logs_by_level(parse_log_list, log_level)
        counts_dict = count_logs_by_level(parse_log_list)
        display_log_counts(counts_dict)

    except FileNotFoundError:
        print("Програма не змогла знайти файл!")
        return (0,0)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return (0,0)
    finally:
        print("Якщо хочете повторити роботу програми, запустіть її заново!")

#print(sys.argv)

#file_path: Path = Path(Path.cwd(), "log.txt")
#file_path: Path = Path(Path.cwd(), sys.argv[1])

# print(file_path)

#load_logs(file_path)
load_logs(Path(sys.argv[1]))
