# Facebook Private Group Crawler

This project target goal is help me to crawl down all the information that I want from Facebook private group. Filter out the post contain specific **target word** , send them to user's LINE.

# Environment
  - **Python 3.8.3** or higher
  - **Ubuntu 20.04.2 LTS**
  - **LINE Notify account**

# Build
1.Install requirements.txt
```
pip3 install -r requirements.txt
```

2.Prepare LINE-notify token

[How to get LINE-notify token](https://bustlec.github.io/note/2018/07/10/line-notify-using-python/)

3. Run
```
python3 crawler.py -a [facebook username/email address] -p [facebook password]
```

# Notes



