import sys

def validate_conf(data: dict[str, str]) -> dict:
    required_keys: list[str] = ["WIDTH", "HEIGHT", "ENTRY", "EXIT", "OUTPUT_FILE", "PERFECT"]
    valid_data: dict = {}
    for key in required_keys:
        if key not in data:
            raise ValueError(f"Missing mandatory key: {key}")
    for key, value in data.items():
        if key == "WIDTH":
            valid_data["WIDTH"] = int(value)
        elif key == "HEIGHT":
            valid_data["HEIGHT"] = int(value)
        elif key == "ENTRY":
            parts = value.split(",")
            valid_data["ENTRY"] = (int(parts[0]), int(parts[1]))
        elif key == "EXIT":
            parts = value.split(",")
            valid_data["EXIT"] = (int(parts[0]), int(parts[1]))
        elif key == "PERFECT":
            valid_data["PERFECT"] = value.lower() in ["true", "1", "yes"]
        else:
            valid_data[key] = value
            
    return valid_data


def sanitize(data: list[str]) -> dict:
    result: dict = {}
    for line in data:
        if len(line) == 0 or line.startswith("#"):
            continue
        temp: list[str] = line.split("=", 1)
        if len(temp) == 2:
            key: str = temp[0].strip().upper()
            value: str = temp[1].strip()
            result[key] = value
    return validate_conf(result)


def parse_config(filename: str) -> dict:
    setting: list = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                setting.append(line.strip())
        final_config: dict = sanitize(setting)
        return final_config
    except FileNotFoundError:
        print(f"Error: Configuration file '{filename}' not found.")
        sys.exit(1)
    except ValueError as error:
        print(f"Error: Invalid configuration format. {error}")
        sys.exit(1)
    except Exception as error:
        print(f"Critical Error: {error}")
        sys.exit(1)