# Facebook Private Group Crawler

<a href="https://hits.seeyoufarm.com"><img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fdrive.google.com%2Fdrive%2Ffolders%2F1T-SRSi5D_dyvJ-HqAEtiHGYdiWfJ6_q8&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false"/></a>

[![Github all releases](https://hits.sh/drive.google.com/drive/folders/1T-SRSi5D_dyvJ-HqAEtiHGYdiWfJ6_q8.svg)]

## Anomaly Backbone Checkpoint Download  
  |   Description  | Weights Download |
  | :------------: | :--------------: |
  | MVTecAD ResNet18 | [Download Link](https://drive.google.com/drive/folders/1T-SRSi5D_dyvJ-HqAEtiHGYdiWfJ6_q8?usp=sharing) |
  | IndustrialDataset ResNet18 | [Download Link](https://drive.google.com/drive/folders/1knOHNj5U5Ya6qRjhD3hUo-K4F_BTg0YS?usp=sharing) |



This project target goal is help me to crawl down all the information that I want from ``Facebook private group``. Filter out the post that contain specific ``target keyword`` , save data into ``Firebase Realtime Database`` and notify user by ``LINE``.

# Environment
  - **Python 3.8.3** or higher
  - **Ubuntu 20.04.2 LTS**
  - **LINE Notify account**
  - **Firebase**

# Build

1.Install requirements.txt

```
pip3 install -r requirements.txt
```

2.Prepare **LINE-notify token**
  
  [How to get LINE-notify token](https://bustlec.github.io/note/2018/07/10/line-notify-using-python/)


3.Prepare **Firebase serviceAccount.json**

  [How to get your Firebase serviceAccount.json and certificate](https://medium.com/pyradise/10%E5%88%86%E9%90%98%E8%B3%87%E6%96%99%E5%BA%AB%E6%93%8D%E4%BD%9C-%E6%96%B0%E5%A2%9E%E8%B3%87%E6%96%99-b96db385e1e4)


4.Run

```
python3 crawler.py -a [facebook username/email address] -p [facebook password]
```

# Result

<p align="center">
  <img src='https://user-images.githubusercontent.com/44123278/126373072-137ccfdb-cd3f-4081-925a-1aa977dcfba7.png'>
</p>


<p align="center">
  <img src='https://user-images.githubusercontent.com/44123278/126373162-6f933c29-4559-4e83-9ec5-b28564698d74.jpg'>
</p>



# Notes
  1. You can set your **specific keyword** in the post that you are looking for in the ``crawler.py``.

  2. This script can work succesfully with **once** a time, and terminate. But cannot execute continuously because Facebook will block you down, and ask you to **verify and relogin** again. So after some consider, I'm not going to make extra features or functions to solve this contidion. There have some better way to accomplish such goal on other website, but not in Facebook. ``API`` is recommended for these requires, but you have to create your own functions API in special require.
  
  3. Atleast in this script, I had learned most of the **crawl** and **scrapy** skill so it is not meaningless to me.

  4. Feel free to contact me if you have any problem or idea!


# References
  - [Crawler tutorial](https://www.learncodewithmike.com/2020/06/python-line-notify.html)
  - [Firebase serviceAccount.json](https://medium.com/pyradise/10%E5%88%86%E9%90%98%E8%B3%87%E6%96%99%E5%BA%AB%E6%93%8D%E4%BD%9C-%E6%96%B0%E5%A2%9E%E8%B3%87%E6%96%99-b96db385e1e4)
  - [Firebase firebase_admin_db module document](https://firebase.google.com/docs/reference/admin/python/firebase_admin.db)
  - [Facebook API](https://developers.facebook.com/docs/groups-api/common-uses#app-installation-webhooks)
