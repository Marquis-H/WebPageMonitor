# WebPageMonitor
定时监控网页访问状态，并上报到telegram通知项目维护人

# Usage
### Clone并复制出config.json
```
# git clone https://github.com/Marquis-H/WebPageMonitor
# cd WebPageMonitor
# cp config.json.dist config.json
```
## 修改config.json
```
{
    "urls": [], // 需要监听的Url
    "tg-chat": "", // tg bot
    "time_interval_num": 5 //监听时间间隔
}
```

# Run
```
python ./Main.py
```