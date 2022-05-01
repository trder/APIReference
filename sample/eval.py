#启动模拟交易
#输入指令：python eval.py donchian
#启动模拟交易
import sys

def load_trading_system():
    '''
    载入交易系统
    '''
    pass

if __name__ == '__main__':
    #获取参数个数
    nargv = len(sys.argv)
    if nargv < 2:
        print("请输入系统名")
        return
    #获取交易系统名
    trading_system_name = sys.argv[1]
    #载入交易系统
    trading_system = load_trading_system(trading_system_name)
    if not trading_system:
        print("交易系统载入失败")
        return
    #评估交易系统
    eval_result = eval_trading_system(trading_system)
    #输出评估结果
    print(eval_result)
