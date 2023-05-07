#!/usr/bin/env python3
import argparse
import os
import pprint

from bs4 import BeautifulSoup

if "__main__" == __name__:
    parser = argparse.ArgumentParser("Blueprint diff")
    parser.add_argument("bad", help="A bad gamestart XML file")
    parser.add_argument("good", help="A good gamestart XML file for comparison")
    args = parser.parse_args()

    with open(os.path.expanduser(args.bad), "r") as f:
        bad = f.read()

    with open(os.path.expanduser(args.good), "r") as f:
        good = f.read()

    bad_soup = BeautifulSoup(bad, "xml")
    good_soup = BeautifulSoup(good, "xml")

    bad_wares = set(bad_soup.gamestarts.gamestart.player.blueprints.find_all("ware"))
    good_wares = set(good_soup.gamestarts.gamestart.player.blueprints.find_all("ware"))

    pprint.pprint(bad_wares.difference(good_wares))
