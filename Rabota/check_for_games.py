all_games = ['age_of_troy', 'almighty_ramses', 'amazons_battle', 'amazons_battle_50', 'ancient_dynasty', 'blue_oceans',
             'book_of_magic', 'brave_cat', 'burning_hot', 'burning_hot_20', 'burning_hot_40', 'burning_hot_40_6_reels',
             'burning_hot_6_reels', 'captain_nemo', 'cats_royal', 'charming_joker_20', 'circus_brilliant', 'dazzling_hot',
             'dazzling_hot_20', 'dice_and_roll', 'dorothys_fairyland', 'dragon_reborn', 'egypt_sky',
             'empress_charm', 'extra_stars', 'extremely_hot', 'flaming_hot', 'flaming_hot_extreme', 'fortune_spells', 'frog_story',
             'game_of_luck', 'genius_of_leonardo', 'gold_dust', 'great_27', 'hot_blast_20', 'imperial_wars', 'joker_reels_20',
             'juggle_fruits_5', 'kingdom_of_fruits', 'lucky_hot', 'lucky_kings_40', 'lucky_wood', 'majestic_forest',
             'mega_clover_40', 'more_dice_and_roll', 'oil_company', 'olympus_glory', 'penguin_style', 'pin_up_queen',
             'rainbow_luck', 'rainbow_queen', 'retro_cabaret', 'rise_of_ra', 'secrets_of_alchemy', 'secrets_of_london', 'shining_crown',
             'spicy_fruits_30', 'story_of_alexander', 'super_hot_100', 'super_hot_20', 'super_hot_40', 'supreme_hot',
             'ultimate_hot', 'vampire_night', 'versailles_gold', 'volcano_wealth', 'white_wolf', 'wins_27', 'wins_81',
             'witches_charm', 'zodiac_wheel']

print("All Games size: ", end=" ")
print(len(all_games))

print()
games_green_mk = ['ps_super_hot_20', 'ps_super_hot_40', 'ps_super_hot_100', 'ps_dazzling_hot', 'ps_burning_hot',
                'ps_burning_hot_40', 'ps_flaming_hot', 'ps_amazons_battle', 'ps_ancient_dynasty', 'ps_pin_up_queen',
                'ps_story_of_alexander', 'ps_almighty_ramses', 'ps_shining_crown', 'ps_mega_clover_40',
                'ps_spicy_fruits_30', 'ps_extra_stars', 'ps_rise_of_ra', 'ps_versailles_gold', 'ps_joker_reels_20',
                'ps_hot_blast_20', 'ps_dorothys_fairyland', 'ps_brave_cat', 'ps_fortune_spells', 'ps_egypt_sky',
                'ps_extremely_hot', 'ps_lucky_kings_40', 'ps_dice_and_roll', 'ps_more_dice_and_roll', 'ps_lucky_hot',
                'ps_ultimate_hot', 'ps_olympus_glory', 'ps_majestic_forest', 'ps_age_of_troy', 'ps_kingdom_of_fruits',
                'ps_secrets_of_alchemy', 'ps_oil_company']

print("Green Games size: ", end=" ")
print(len(games_green_mk))
print()

games_red_mk = ['ps_super_hot_20', 'ps_super_hot_40', 'ps_burning_hot', 'ps_dazzling_hot', 'ps_flaming_hot',
                'ps_amazons_battle', 'ps_amazons_battle_50', 'ps_pin_up_queen', 'ps_story_of_alexander', 'ps_joker_reels_20',
                'ps_spicy_fruits_30', 'ps_mega_clover_40', 'ps_shining_crown', 'ps_versailles_gold',
                'ps_dice_and_roll', 'ps_extra_stars', 'ps_rise_of_ra', 'ps_fortune_spells', 'ps_burning_hot_40',
                'ps_hot_blast_20', 'ps_frog_story', 'ps_almighty_ramses', 'ps_captain_nemo', 'ps_dorothys_fairyland',
                'ps_charming_joker_20', 'ps_dazzling_hot_20', 'ps_lucky_hot', 'ps_ultimate_hot', 'ps_juggle_fruits_5',
                'ps_zodiac_wheel', 'ps_ancient_dynasty', 'ps_gold_dust', 'ps_imperial_wars', 'ps_olympus_glory',
                'ps_game_of_luck', 'ps_penguin_style', 'ps_brave_cat', 'ps_extremely_hot', 'ps_wins_27', 'ps_great_27',
                'ps_secrets_of_alchemy', 'ps_supreme_hot', 'ps_white_wolf', 'ps_book_of_magic', 'ps_dragon_reborn',
                'ps_witches_charm', 'ps_egypt_sky', 'ps_wins_81']

print("Red Games size: ", end=" ")
print(len(games_red_mk))
print()

games_purple_mk = ['ps_super_hot_20', 'ps_super_hot_40', 'ps_burning_hot', 'ps_dazzling_hot', 'ps_flaming_hot',
                'ps_amazons_battle', 'ps_burning_hot_6_reels', 'ps_rainbow_luck', 'ps_flaming_hot_extreme', 'ps_volcano_wealth',
                'ps_burning_hot_20', 'ps_vampire_night', 'ps_shining_crown', 'ps_mega_clover_40',
                'ps_burning_hot_40', 'ps_extra_stars', 'ps_rise_of_ra', 'ps_versailles_gold', 'ps_burning_hot_40_6_reels',
                'ps_cats_royal', 'ps_lucky_wood', 'ps_almighty_ramses', 'ps_spicy_fruits_30', 'ps_super_hot_100',
                'ps_charming_joker_20', 'ps_dazzling_hot_20', 'ps_lucky_hot', 'ps_ultimate_hot', 'ps_dice_and_roll',
                'ps_more_dice_and_roll', 'ps_amazons_battle_50', 'ps_blue_oceans', 'ps_lucky_kings_40', 'ps_genius_of_leonardo',
                'ps_secrets_of_london', 'ps_retro_cabaret', 'ps_brave_cat', 'ps_circus_brilliant', 'ps_rainbow_queen', 'ps_empress_charm',
                'ps_secrets_of_alchemy', 'ps_fortune_spells', 'ps_captain_nemo', 'ps_kingdom_of_fruits', 'ps_ancient_dynasty',
                'ps_olympus_glory', 'ps_egypt_sky', 'ps_dorothys_fairyland']

print("Purple Games size: ", end=" ")
print(len(games_purple_mk))
print()

result = []
for elem in all_games:
    for green in games_green_mk:
        check_var = 'ps_' + elem
        if green == check_var:
            games_green_mk.remove(green)
           # print(f"{green} == {check_var}")
            result.append(green)

print(len(result))
print("Left Games in Green: ")
print(games_green_mk)


result = []
for elem in all_games:
    for game in games_red_mk:
        check_var = 'ps_' + elem
        if game == check_var:
            games_red_mk.remove(game)
           # print(f"{game} == {check_var}")
            result.append(game)

print(len(result))
print("Left Games in Red: ")
print(games_red_mk)


result = []
for elem in all_games:
    for game in games_purple_mk:
        check_var = 'ps_' + elem
        if game == check_var:
            games_purple_mk.remove(game)
           # print(f"{game} == {check_var}")
            result.append(game)

print(len(result))
print("Left Games in Purple: ")
print(games_purple_mk)
