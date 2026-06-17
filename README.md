# turtlesim_square

ROS Noetic 小海龟画正方形练习

## 节点结构

- **`draw_square.py`**  
  发布 `/turtle1/cmd_vel` 话题（`geometry_msgs/Twist`），控制小海龟按正方形轨迹移动。
  循环执行：直线前进 → 原地转弯90° → 重复4次。

## 启动方式

```bash
# 终端1：启动 ROS 核心
roscore

# 终端2：启动小海龟仿真器
rosrun turtlesim turtlesim_node

# 终端3：运行画正方形节点
rosrun turtlesim_square draw_square.py
```

## 效果

小海龟以边长2单位、线速度1单位/秒走出正方形轨迹。
