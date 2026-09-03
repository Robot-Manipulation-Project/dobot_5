# dobot_5

ROS 2 workspace for visualizing robot models in RViz, including a Dobot-style arm model and a simple Cartesian robot model.

## Repository Layout

- `src/dobot_viz` — Dobot visualization package (`dobot.urdf.xacro`, launch files)
- `src/robot_viz` — Example robot visualization package (`robot1.urdf.xacro`, `robots.rviz`, launch file)
- `build/`, `install/`, `log/` — Generated colcon build artifacts

## Prerequisites

- ROS 2 (tested as an ament/colcon workspace)
- `colcon`
- ROS packages used by this workspace:
  - `robot_state_publisher`
  - `joint_state_publisher` / `joint_state_publisher_gui`
  - `rviz2`
  - `xacro`

## Build

From the repository root:

```bash
colcon build
```

## Use

Source the workspace:

```bash
source install/setup.bash
```

Launch the Dobot visualization:

```bash
ros2 launch dobot_viz dobot_viz_launch.xml
```

Launch the alternative Dobot twin setup:

```bash
ros2 launch dobot_viz dobot_twin_viz_launch.xml
```

Launch the example robot visualization:

```bash
ros2 launch robot_viz robots_viz_launch.xml
```

## Test

Run package tests and linters:

```bash
colcon test
colcon test-result --verbose
```

## Notes

This repository includes committed `build/`, `install/`, and `log/` directories from previous workspace builds.
