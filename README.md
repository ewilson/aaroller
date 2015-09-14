# aaroller
command line dice roller for axis &amp; allies

### How to use:

    $ python3 main.py
    >> a_roll 12 2
    Hits: 3
    Rolls:  3  5 [1][1][1] 6  3  3  5  4  4  6 
    >> x_roll 8 3
    Hits: 7
    Rolls: [3] 4 [1][1][1][3][3][3]
    >> stats
    Allies>> Expected Hits:    4.0, Hits:    3, Rolls:   12, Luck %:  -8.3%
      Axis>> Expected Hits:    4.0, Hits:    7, Rolls:    8, Luck %:  37.5%

The idea should be pretty simple if you have played Axis and Allies. The only difference between the `a_roll`
and the `x_roll` command is where the results are recorded for stats purposes ... so your complaints about bad
luck can be supported with real data.
    
