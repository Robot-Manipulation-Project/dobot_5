import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/mnt/d/Curtin_Colombo/year_3/sem_1/mxen3005/milestone_5_redone/mxen_ws/install/robot_viz'
