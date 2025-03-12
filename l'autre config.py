#!/bin/python3

import os
import argparse

parser = argparse.ArgumentParser(description='Config trackmania server')
parser.add_argument('-m', '--maps', type=str, help='Maps location in compose/maps directory')
parser.add_argument('-o', '--map-order', type=bool, default=False, help='Is the map order random ?')
parser.add_argument('-p', '--points-limit', type=int, default=100, help='Points limit for the match')
parser.add_argument('-r', '--points-repartition', type=str, default="10,7,5,3", help='Points repartitino for the match (ex: 10,6,4,3,2,1)')
parser.add_argument('-w', '--nb-winners', type=int, default=3, help='Number of winners for the match')
parser.add_argument('-R', '--rounds-per-map', type=int, default=4, help='Number of rounds per map for the match')
parser.add_argument('-t', '--finish-to', type=int, default=15, help='Finish time out for the match')
parser.add_argument('-d', '--warmup-duration', type=int, default=-1, help='Warmup duration for the match')
parser.add_argument('-n', '--nb-warmup', type=int, default=1, help='Number of warmup for the match')
parser.add_argument('-s', '--min-players', type=int, default=4, help='Minimum players count for the match')
args = parser.parse_args()

maps_rel_location = args.maps
print("Maps location: ", maps_rel_location)
if not maps_rel_location:
    maps_abs_location = os.path.join(os.getcwd(), 'compose', 'maps')
else:
    maps_abs_location = os.path.join(os.getcwd(), 'compose', 'maps', maps_rel_location)

map_list = os.listdir(maps_abs_location)
if not map_list:
    print("No maps found in the directory")
    exit(1)
map_dic = {}
print("Maps: ")
for i,map in enumerate(map_list):
    print(f"   {i} - {map}")
    map_dic[i] = map

file_to_paste = f"""<?xml version="1.0" encoding="utf-8"?>
<playlist>
        <gameinfos>
                <game_mode>0</game_mode>
                <script_name>Trackmania/TM_Cup_Online</script_name>
        </gameinfos>
        <filter>
                <is_lan>1</is_lan>
                <random_map_order>{1 if args.map_order else 0}</random_map_order>
        </filter>
        <script_settings>
                <setting name="S_PointsLimit" type="integer" value="{args.points_limit}" />
                <setting name="S_PointsRepartition" type="text" value="{args.points_repartition}" />
                <setting name="S_NbWinners" type="integer" value="{args.nb_winners}" />
                <setting name="S_RoundsPerMap" type="integer" value="{args.rounds_per_map}" />
                <setting name="S_FinishTimeout" type="integer" value="{args.finish_to}" />
                <setting name="S_WarmUpDuration" type="integer" value="{args.warmup_duration}" />
                <setting name="S_WarmUpNb" type="integer" value="{args.nb_warmup}" />
                <setting name="S_NbOfPlayersMin" type="integer" value="{args.min_players}" />
        </script_settings>
        <startindex>0</startindex>
"""
for i in input("Ordered map list (separated by ','): ").split(","):
    map = map_dic[int(i)]
    file_to_paste += f"""
        <map>
                <file>{maps_rel_location}/{map}</file>
        </map>
"""
file_to_paste += "</playlist>"

for dir in os.listdir(os.path.join(os.getcwd(), 'compose')):
    if dir.__contains__('cup'):
        print("Updating", dir, "...")
        with open(os.path.join(os.getcwd(), 'compose', dir, 'maps', 'MatchSettings', 'cfg_tracklist.xml'), 'w') as f:
            f.write(file_to_paste)
