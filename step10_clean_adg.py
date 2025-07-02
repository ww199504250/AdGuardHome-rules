from pathlib import Path
import tempfile
import shutil

# === 路径 ===
src = Path('./output/BlackList.txt')              # 要清理的原文件
log = Path('./temp/Log/clean_adg.log')       # 删除行日志
log.parent.mkdir(parents=True, exist_ok=True)

# === 流式处理，避免一次性占用大量内存 ===
with src.open(encoding='utf-8') as fin, \
     tempfile.NamedTemporaryFile('w', delete=False, dir=src.parent, encoding='utf-8') as tmp, \
     log.open('w', encoding='utf-8') as flog:
    for line in fin:
        if '.js^' in line:
            flog.write(line)     # 记录被删行
        else:
            tmp.write(line)      # 写入临时文件

# === 原子替换：临时文件 → 覆盖原文件 ===
shutil.move(tmp.name, src)

print(f'✅ 处理完成，已覆盖 {src} ；删除日志 → {log}')
