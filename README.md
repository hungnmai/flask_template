## Template cho Flask
**Project bao gồm các module:**
* ai: Phần xử lý logic
* api: cung cấp api, router
* database: DB đang sử dụng là mongoDB

### Cài đặt các thư viện

**Tạo môi trường bằng conda**
```bash
conda create -n name_env python=3.6
``` 
**Sau khi tạo môi trường thực hiện activate:**

```bash
conda activate name_env
```

**cd vào project và cài đặt thư viện bằng lệnh:**
```bash
pip install -r requiments.txt
```

### Chạy template:
```bash
python start.py
```
*Note: có thể thay host và port trong file config.yaml*