#启动模拟交易
#输入指令：python eval.py donchian
#启动模拟交易
import sys

gpus = sys.argv[1]

if __name__ == '__main__':
    #获取参数个数
    nargv = len(sys.argv)
    if nargv < 2:
        print("请输入系统名")
        return
    #载入交易系统
    load_trading_system()
