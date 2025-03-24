# Financial Modelling

This repository is for educational purposes only and contains only my own work, open source code, and domain knowledge available online.

[License](license.txt)

## Documentation

- [Introduction](quantitative/documentation/finance/1_introduction.md)
- [Interest Rates](quantitative/documentation/finance/2_interest-rates.md)
- [Bonds](quantitative/documentation/finance/3_bonds.md)
- [Equities](quantitative/documentation/finance/4_equities.md)
- [Commodities](quantitative/documentation/finance/5_commodities.md)
  - [Commodity Derivatives](quantitative/documentation/finance/commodities/commodity_derivatives.md)
- [Arbitrage](quantitative/documentation/finance/6_arbitrage.md)
- [Forwards, Futures, and Swaps](quantitative/documentation/finance/7_forwards_futures_swaps.md)
- [Stochastic Processes](quantitative/documentation/finance/8_stochastic-processes.md)
- [Options](quantitative/documentation/finance/9_options.md)

## Reading List and References

- [1] J. Hull, Options, Futures and Other Derivatives. Pearson/Prentice Hall, 2009.
- [2] R. C. Martin and M. Martin, Agile Principles, Patterns, and Practices in C#. Pearson Education, 2006.

## Useful Links

- [Option Strategies Quick Guide](https://www.theocc.com/getmedia/f34f8a0d-806f-4f1a-adf7-d49d8d94b16e/option-strategies-quick-guide.pdf)
- [Options Playbook](https://www.optionsplaybook.com/)
- [Derivatives Academy](https://bookdown.org/maxime_debellefroid/MyBook/)
- [Modelling and Estimating Commodity Prices: Copper Prices](https://www.math.ucdavis.edu/~rjbw/mypage/Mathematics_of_Finance_files/WtsR13.pdf)
- [Futures Fundamentals](https://www.futuresfundamentals.org/)
- [Derivatives](https://financetrainingcourse.com/education/derivatives/)
- [Derivatives Crash Course](https://financetrainingcourse.com/education/the-derivatives-crash-course-for-dummies/)
- [Financial Risk Modelling](https://financetrainingcourse.com/education/risk-model/)

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

## PostgreSQL Commands

To stop the PostgreSQL service:

    sudo systemctl stop postgresql

To start PostgreSQL:

    sudo systemctl start postgresql

To restart PostgreSQL (useful after configuration changes):

    sudo systemctl restart postgresql

To check whether PostgreSQL is running or stopped:

    sudo systemctl status postgresql

Disable automatic startup on boot:

    sudo systemctl disable postgresql

Enable automatic startup on boot:

    sudo systemctl enable postgresql

Check active PostgreSQL connections:

    sudo -u postgres psql -c "SELECT datname, pid, usename, application_name, client_addr FROM pg_stat_activity;"

Find PostgreSQL port and listen addresses:

    sudo cat /etc/postgresql/*/main/postgresql.conf | grep -E 'listen_addresses|port'

Check PostgreSQL processes:

    ps aux | grep postgres
