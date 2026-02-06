def validate_conf(data: dict[str, str]):
    required_keys = ["WIDTH", "HEIGHT", "ENTRY",
        "EXIT", "OUTPUT_FILE", "PERFECT"]
    valid_data = {}
    for key in required_keys:
        if key not in data:
            raise ValueError(f"Missing mandatory key {key}")
    if "WIDTH" in data:
        valid_data["WIDTH"] = int(data["WIDTH"])
    if "HEIGHT" in data:
        valid_data["HEIGHT"] = int(data["HEIGHT"])
    if "ENTRY" in data:
        parts = data["ENTRY"].split(",")
        valid_data["ENTRY"] = (int(parts[0]), int(parts[1]))
    if "EXIT" in data:
        parts = data["ENTRY"].split(",")
        valid_data["ENTRY"] = (int(parts[0]), int(parts[1]))
    if "PERFECT" in data:
        if data["PERFECT"] == "True":
            valid_data["PERFECT"] = True
        else:
            valid_data["PERFECT"] = False
    if "OUTPUT_FILE" in data:
        valid_data["OUTPUT_FILE"] = data["OUTPUT_FILE"]
    return valid_data


def sanitize(data: list[str]):
    result = {}
    for x in range(len(data)):
        line = data[x]
        if len(line) == 0 or line.startswith("#"):
            continue
        temp = line.split("=")
        if len(temp) == 2:
            key = temp[0].strip()
            value = temp[1].strip()
            result[key] = value
    return validate_conf(result)


def parse_config(filename: str):
    setting = []
    try:
        with open(filename, 'r') as file:
            for x in file:
                setting.append(x.strip())
        final_config = sanitize(setting)
        print(final_config)
    except FileNotFoundError as error:
        return error
