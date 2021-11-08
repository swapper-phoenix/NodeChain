#!/usr/bin/python3
import sys
import os
import argparse


def queryYesNo(question, default="yes"):
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n]: "
    elif default == "yes":
        prompt = " [Y/n]: "
    elif default == "no":
        prompt = " [y/N]: "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write(
                "Please respond with 'yes' or 'no' (or 'y' or 'n').\n")


def queryPort(question):
    while True:
        sys.stdout.write(question)
        port = input().lower()
        if not port.isnumeric():
            sys.stdout.write(
                "Port must be a number, please respond with a valid port. \n")
        else:
            return port


def queryPath(coin, stage):
    try:
        path = input("Please choose the directory to save blockchain data " +
                     f"(/srv/swapper-node/{coin}_{stage}): ")
    except SyntaxError:
        path = f"/srv/swapper-node/{coin}_{stage}"
    if not path:
        path = f"/srv/swapper-node/{coin}_{stage}"
    return path


def queryCerts(certs):
    if not certs:
        try:
            sys.stdout.write("WARN: Please note that you need to have the files swapper_cert.key and swapper_cert.crt in "
                             "the certificates directory.\n")
            path = input("Please choose the path of the certs " +
                         f"(/etc/ssl/certs): ")
        except SyntaxError:
            path = f"/etc/ssl/certs"
        if not path:
            path = f"/etc/ssl/certs"
    else:
        path = certs
    return path


def askSSL(config, certs):
    if config:
        while True:
            path = queryCerts(certs)

            if os.path.isdir(path) and "swapper_cert.key" in os.listdir(path) and "swapper_cert.crt" in os.listdir(path):
                os.environ["CERT_PATH"] = path
                os.environ["NGINX_CONFIG_PATH"] = "../../nginx/ssl.conf"
                return
    elif not config:
        os.environ["NGINX_CONFIG_PATH"] = "../../nginx/nginx.conf"
        os.environ["CERT_PATH"] = "/etc/ssl/certs"
        return
    else:
        while True:
            if queryYesNo("Do you want to activate SSL? ", "no"):
                path = queryCerts(certs)

                if os.path.isdir(path) and "swapper_cert.key" in os.listdir(path) and "swapper_cert.crt" in os.listdir(path):
                    os.environ["CERT_PATH"] = path
                    os.environ["NGINX_CONFIG_PATH"] = "../../nginx/ssl.conf"
                    return
                else:
                    sys.stdout.write("You need to have the files swapper_cert.key and swapper_cert.crt in the "
                                     "certificates directory. \n")
            else:
                os.environ["NGINX_CONFIG_PATH"] = "../../nginx/nginx.conf"
                os.environ["CERT_PATH"] = "/etc/ssl/certs"
                return


def fillMenu(listFnc, choiceFnc, exitFnc):
    menu = {}
    counter = 1
    for item in listFnc():
        menu[str(counter)] = (item, choiceFnc)
        counter += 1

    menu[str(len(listFnc()) + 1)] = ("Exit", exitFnc)

    return menu


def showMainTitle():
    print(r"---------------------------------------------------")
    print(r"  _  _          _        ___  _                   ")
    print(r" | \| | ___  __| | ___  / __|| |_   __ _ (_) _ _  ")
    print(r" | .` |/ _ \/ _` |/ -_)| (__ | ' \ / _` || || ' \ ")
    print(r" |_|\_|\___/\__,_|\___| \___||_||_|\__,_||_||_||_|")
    print(r"---------------------------------------------------")


def showSubtitle(subtitle):
    print("===================================================")
    print(f"\t\t{subtitle}")
    print("===================================================")


def signalHandler(sig, frame):
    print('Exiting gracefully, goodbye!')
    sys.exit(0)


def argumentHandler():
    parser = argparse.ArgumentParser(
        description='Nodechain allows the user to build and manage their own nodes natively without having to rely on external services.', prog="python3 nodechain.py")
    parser.add_argument('-t', '--token', action="store",
                        dest='token', help="symbol of the token", default=None)
    parser.add_argument('-n', '--network', action="store", dest='network',
                        help="network where to set up the blockchain", choices=['mainnet', 'testnet', 'development'], default=None)
    parser.add_argument('-p', '--port', action="store", dest='port',
                        help="port to start the node", default=None)
    parser.add_argument('-sp', '--sslport', action="store",
                        dest='ssl_port', help="ssl port", default=None)
    parser.add_argument('-b', '--blockchain', action="store", dest='blockchain_path',
                        help="path to store blockchain files", default=None)
    parser.add_argument('--ssl', action="store_true",
                        dest='config', help="ssl config", default=None)
    parser.add_argument('--no-ssl', action="store_false",
                        dest='config', help="no ssl config", default=None)
    parser.add_argument('-c', '--cert', action="store",
                        dest='certs', help="path to certs", default=None)
    parser.add_argument('-v', '--version', action="version",
                        version="NodeChain version 1.1.1", help="software version ", default=None)

    args = parser.parse_args()

    return args
