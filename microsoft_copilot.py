import os
import yaml

def load_config(config_file):
    with open(config_file, 'r') as f:
        config = yaml.safe_load(f)
    return config

def rename_files(config):
    for target_dir in config.get('target_dirs', []):
        dir_name = target_dir.get('dir_name')
        prefix = target_dir.get('prefix', '')
        suffix = target_dir.get('suffix', '')

        if not os.path.exists(dir_name):
            print(f"Directory '{dir_name}' does not exist.")
            continue

        for filename in os.listdir(dir_name):
            if os.path.isfile(os.path.join(dir_name, filename)):
                new_filename = f"{prefix}{filename}{suffix}"
                os.rename(os.path.join(dir_name, filename), os.path.join(dir_name, new_filename))
                print(f"Renamed '{filename}' to '{new_filename}' in '{dir_name}'.")

if __name__ == "__main__":
    config_file = "config.yaml"  # Specify the path to your YAML config file
    config = load_config(config_file)
    rename_files(config)
