# coding:utf8

###########################################

### 功能：从工程目录中提取，集数 ，卡号，等数据
### 命名规则：片集名_镜头号_文件类型.文件扩展名

###########################################

import os
import re


class ProjectData():
    def __init__(self, project_dir, ani_folder_name = "Animation", asset_folder_name = "Asset"):
        self.animation_dir = project_dir + os.sep + ani_folder_name
        self.asset_dir = project_dir + os.sep + asset_folder_name

        self.getEpsodeData()
        self.getShotData()

    def getEpsodeData(self):
        # 获取动画文件夹路径下的子文件夹，即片集的名称及数量
        self.episode_list = os.listdir(self.animation_dir)
        # episode_count = len(self.episode_list)
        self.episode_dir_list = {self.animation_dir + os.sep + episode for episode in self.episode_list}

    def getShotData(self):
        # shot_name_list 例：Shot003
        self.shot_name_list = []
        # error_list 不符合命名规范的文件名 列：EP003_SHOT_001_Ani.ma
        self.error_list = []
        episode_count = 0

        for episode_dir in self.episode_dir_list:
            shot_list = os.listdir(episode_dir)
            episode_count += 1
            for shot_name in shot_list:

                # 正则表达式命名规则 例：EP030_SHOT008_ANI.ma
                match_result = re.match("(?P<episode>[A-Za-z0-9]+)"
                                        "_(?P<shot>[A-Za-z0-9]+)"
                                        "_(?P<type>[A-Za-z]+)\.\w+",
                                        shot_name)
                if match_result != None:
                    if match_result.group("shot") not in shot_list:
                        self.shot_name_list.append(match_result.group("shot"))

                    else:
                        pass

                else:
                    self.error_list.append(shot_name)

            # print self.episode_list[episode_count - 1]
            # print self.shot_name_list

    def saveData(slef):
        # TODO: 把数据保存为临时文件好让主窗口的表格提取数据。
        # shot_file_data = {"episode":episode_list, "episode_count":len(episode_list),
        #                   "shot":shot_list, "shot_count":len(shot_list),
        #                   "error":error_list, "error_count":len(error_list)}
        # return shot_file_data
        pass

if __name__ == "__main__":
    test = ProjectData(r'D:\Ben\Python\Rendering_Management\core\Test_File')
