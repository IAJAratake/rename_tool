import os
import yaml
import argparse


def load_config(config_file):
    with open(config_file, 'r') as f:
        config = yaml.safe_load(f)
    return config


def process_files(dir_config):
    dir_name = dir_config['dir_name']
    prefix = dir_config['prefix']
    suffix = dir_config['suffix']

    processed_files = []

    # ディレクトリ内のファイルを処理する
    for filename in os.listdir(dir_name):
        # ファイルのフルパスを取得
        src_path = os.path.join(dir_name, filename)

        # ディレクトリの場合は無視
        if os.path.isdir(src_path):
            continue

        # 新しいファイル名を作成
        base, ext = os.path.splitext(filename)
        new_filename = f"{prefix}{base}{suffix}{ext}"
        dst_path = os.path.join(dir_name, new_filename)

        # ファイル名を変更
        os.rename(src_path, dst_path)
        processed_files.append((src_path, dst_path))

    return processed_files


def process_directories(config):
    for dir_config in config['target_dirs']:
        processed_files = process_files(dir_config)
        for src_path, dst_path in processed_files:
            print(f"{src_path} -> {dst_path}")


# メイン処理
parser = argparse.ArgumentParser(description='Rename files in directories')
parser.add_argument('config_file', help='Path to the configuration file')
args = parser.parse_args()

config = load_config(args.config_file)
process_directories(config)