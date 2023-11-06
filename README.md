# Financial Modelling

This repository contains only my own work, open source code, and domain knowledge available online.

The purpose of this repository is for educational purposes only.

[License](license.txt)

## Documentation

- [Introduction](quant-library/documentation/1_introduction.md)
- [Interest Rates](quant-library/documentation/2_interest-rates.md)
- [Bonds](quant-library/documentation/3_bonds.md)
- [Equities](quant-library/documentation/4_equities.md)
- [Commodities](quant-library/documentation/5_commodities.md)
- [Arbitrage](quant-library/documentation/6_arbitrage.md)
- [Derivatives](quant-library/documentation/7_derivatives)

## Git Commands

View git remotes:

    git remote -v

Rename git remote:

    git remote rename <old_name> <new_name>

Git add second remote repo:

    git remote add <name> <url>

Git push to second remote repo:

    git push <remote_name> <branch_name>

If Git repo breaks run the following:

    find .git/objects/ -size 0 -exec rm -f {} \;

    git fetch origin
