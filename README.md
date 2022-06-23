## Template for Flask
**Project includes modules:**
* ai, api, database

### Install requirements

**Create env by conda**
```bash
conda create -n name_env python=3.8
``` 
**activate env:**

```bash
conda activate name_env
```

**Install libs in file requirements:**
```bash
pip install -r requiments.txt
```

### Run service:
```bash
sh start.sh
```
*Note: change config (host, port, worker, timeout ...) in **start.sh***