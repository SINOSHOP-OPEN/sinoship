\"\"\"SINOSHIP 主程序入口\"\"\"
from src.ship import Ship

def main():
    print(\"欢迎使用 SINOSHIP 船舶与航运开源项目！\")
    my_ship = Ship(\"Titanic\", 269)
    print(my_ship.info())

if __name__ == \"__main__\":
    main()
