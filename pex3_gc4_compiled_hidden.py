def initialize_simulation (O00000000O00OOO00 ):#line:4
    global time_elapsed ,fuel_consumed #line:5
    initialize_terrain (O00000000O00OOO00 )#line:6
    initialize_boat (O00000000O00OOO00 )#line:7
    initialize_rocket (O00000000O00OOO00 )#line:8
    time_elapsed =0 #line:9
    fuel_consumed =0 #line:10
def initialize_terrain (O0OOO0OO000O00O0O ):#line:16
    global terrain_list ,GROUND_LENGTH ,GROUND_HEIGHT ,WATER_HEIGHT #line:17
    if O0OOO0OO000O00O0O ==True :#line:19
        terrain_list =[]#line:20
        GROUND_LENGTH =random .randint (0.1 *WINDOW_WIDTH ,0.2 *WINDOW_WIDTH )#line:22
        GROUND_HEIGHT =random .randint (100 ,int (0.4 *WINDOW_HEIGHT ))#line:23
        WATER_HEIGHT =random .randint (50 ,GROUND_HEIGHT )#line:24
        for OO000O0O000O00O00 in range (0 ,WINDOW_WIDTH ):#line:26
            if OO000O0O000O00O00 >GROUND_LENGTH :#line:27
                terrain_list .append (WATER_HEIGHT )#line:28
            else :#line:29
                terrain_list .append (GROUND_HEIGHT )#line:30
def initialize_boat (O0OO00O000OOOO000 ):#line:36
    global boat_start_x ,boat_start_y ,boat_start_vx ,boat_x ,boat_y ,boat_vx #line:37
    if O0OO00O000OOOO000 ==True :#line:39
        boat_start_x =random .randint (WINDOW_WIDTH *0.5 ,WINDOW_WIDTH -BOAT_WIDTH )#line:40
        boat_start_y =WINDOW_HEIGHT -WATER_HEIGHT #line:41
        boat_start_vx =random .random ()*2.0 -1.0 #line:42
    boat_x =boat_start_x #line:44
    boat_y =boat_start_y #line:45
    boat_vx =boat_start_vx #line:46
def initialize_rocket (O0000OOOOO000OOOO ):#line:52
    global rocket_x ,rocket_y ,rocket_vx ,rocket_vy ,rocket_boosting #line:53
    rocket_x =GROUND_LENGTH *0.5 #line:54
    rocket_y =WINDOW_HEIGHT -GROUND_HEIGHT #line:55
    rocket_vx =0 #line:56
    rocket_vy =0 #line:57
    rocket_boosting =True #line:58
def erase_objects ():#line:64
    pythonGraph .clear_window (pythonGraph .colors .BLACK )#line:65
def draw_objects ():#line:71
    draw_terrain ()#line:72
    draw_boat ()#line:73
def initialize_simulation (OOO00OO00OO00O000 ):#line:76
    global time_elapsed ,fuel_consumed #line:77
    initialize_terrain (OOO00OO00OO00O000 )#line:78
    initialize_boat (OOO00OO00OO00O000 )#line:79
    initialize_rocket (OOO00OO00OO00O000 )#line:80
    time_elapsed =0 #line:81
    fuel_consumed =0 #line:82
def initialize_terrain (O0O000O0OO0O0OO0O ):#line:88
    global terrain_list ,GROUND_LENGTH ,GROUND_HEIGHT ,WATER_HEIGHT #line:89
    if O0O000O0OO0O0OO0O ==True :#line:91
        terrain_list =[]#line:92
        GROUND_LENGTH =random .randint (0.1 *WINDOW_WIDTH ,0.2 *WINDOW_WIDTH )#line:94
        GROUND_HEIGHT =random .randint (100 ,int (0.4 *WINDOW_HEIGHT ))#line:95
        WATER_HEIGHT =random .randint (50 ,GROUND_HEIGHT )#line:96
        for O000000OOOO0OOO00 in range (0 ,WINDOW_WIDTH ):#line:98
            if O000000OOOO0OOO00 >GROUND_LENGTH :#line:99
                terrain_list .append (WATER_HEIGHT )#line:100
            else :#line:101
                terrain_list .append (GROUND_HEIGHT )#line:102
def initialize_boat (OOOO00O0OO00O00O0 ):#line:108
    global boat_start_x ,boat_start_y ,boat_start_vx ,boat_x ,boat_y ,boat_vx #line:109
    if OOOO00O0OO00O00O0 ==True :#line:111
        boat_start_x =random .randint (WINDOW_WIDTH *0.5 ,WINDOW_WIDTH -BOAT_WIDTH )#line:112
        boat_start_y =WINDOW_HEIGHT -WATER_HEIGHT #line:113
        boat_start_vx =random .random ()*2.0 -1.0 #line:114
    boat_x =boat_start_x #line:116
    boat_y =boat_start_y #line:117
    boat_vx =boat_start_vx #line:118
def initialize_rocket (O00O0OOOOO00OOOOO ):#line:124
    global rocket_x ,rocket_y ,rocket_vx ,rocket_vy ,rocket_boosting #line:125
    rocket_x =GROUND_LENGTH *0.5 #line:126
    rocket_y =WINDOW_HEIGHT -GROUND_HEIGHT #line:127
    rocket_vx =0 #line:128
    rocket_vy =0 #line:129
    rocket_boosting =True #line:130
def erase_objects ():#line:136
    pythonGraph .clear_window (pythonGraph .colors .BLACK )#line:137
def draw_objects ():#line:143
    draw_terrain ()#line:144
    draw_boat ()#line:145
    draw_rocket ()#line:146
    draw_hud ()#line:147
def draw_terrain ():#line:153
    for O0O0OO00OOO0O0O0O in range (0 ,WINDOW_WIDTH ):#line:154
        if O0O0OO00OOO0O0O0O >GROUND_LENGTH :#line:155
            pythonGraph .draw_line (O0O0OO00OOO0O0O0O ,WINDOW_HEIGHT ,O0O0OO00OOO0O0O0O ,WINDOW_HEIGHT -terrain_list [O0O0OO00OOO0O0O0O ],"light_blue")#line:156
        else :#line:157
            pythonGraph .draw_line (O0O0OO00OOO0O0O0O ,WINDOW_HEIGHT ,O0O0OO00OOO0O0O0O ,WINDOW_HEIGHT -terrain_list [O0O0OO00OOO0O0O0O ],"green")#line:158
def draw_boat ():#line:164
    pythonGraph .draw_image ("boat.png",boat_x ,boat_y -25 ,BOAT_WIDTH ,BOAT_HEIGHT )#line:165
def draw_rocket ():#line:171
    pythonGraph .draw_image ("rocket.png",rocket_x -ROCKET_WIDTH /2 ,rocket_y -ROCKET_HEIGHT ,ROCKET_WIDTH ,ROCKET_HEIGHT )#line:172
    if rocket_thrust_up >0 :#line:173
        pythonGraph .draw_circle (rocket_x ,rocket_y ,4 ,"YELLOW",True )#line:174
    if rocket_thrust_right >0 :#line:175
        pythonGraph .draw_circle (rocket_x -ROCKET_WIDTH /3 ,rocket_y -ROCKET_HEIGHT /5 ,4 ,"YELLOW",True )#line:176
    if rocket_thrust_left >0 :#line:177
        pythonGraph .draw_circle (rocket_x +ROCKET_WIDTH /3 ,rocket_y -ROCKET_HEIGHT /5 ,4 ,"YELLOW",True )#line:178
    if rocket_y <0 :#line:179
        pythonGraph .draw_line (rocket_x -ROCKET_WIDTH /2 ,5 ,rocket_x +ROCKET_WIDTH /2 ,5 ,"YELLOW",5 )#line:180
def draw_hud ():#line:185
    pythonGraph .draw_text ("Max Score: "+str (round (max_score ,1 )),0 ,0 ,"WHITE")#line:186
    pythonGraph .draw_text ("Time Elapsed: "+str (time_elapsed ),0 ,25 ,"WHITE")#line:187
    pythonGraph .draw_text ("Fuel Consumed: "+str (round (fuel_consumed ,2 )),0 ,50 ,"WHITE")#line:188
    pythonGraph .draw_text ("X Velocity: "+str (round (rocket_vx ,2 )),0 ,75 ,"WHITE")#line:189
    pythonGraph .draw_text ("Y Velocity: "+str (round (rocket_vy ,2 )),0 ,100 ,"WHITE")#line:190
    pythonGraph .draw_text ("Crashes: "+str (num_crashes )+"  Landings: "+str (num_landings ),0 ,125 ,"WHITE")#line:191
def update_objects ():#line:196
    update_boat ()#line:197
    update_rocket ()#line:198
def update_rocket ():#line:204
    global rocket_x ,rocket_y ,rocket_vy ,rocket_vx ,rocket_boosting ,rocket_thrust_up ,rocket_thrust_right ,rocket_thrust_left ,fuel_consumed #line:205
    if rocket_boosting ==True :#line:208
        rocket_thrust_up =0 #line:210
        rocket_thrust_right =0 #line:211
        rocket_thrust_left =0 #line:212
        if rocket_y <WINDOW_HEIGHT /2 :#line:214
            rocket_thrust_right =0.25 #line:215
        else :#line:216
            rocket_thrust_up =0.35 #line:217
        if rocket_x >GROUND_LENGTH :#line:219
            rocket_boosting =False #line:220
    rocket_vy -=rocket_thrust_up #line:223
    rocket_vx -=abs (rocket_thrust_left )#line:224
    rocket_vx +=abs (rocket_thrust_right )#line:225
    fuel_consumed =fuel_consumed +abs (rocket_thrust_up )+abs (rocket_thrust_right )+abs (rocket_thrust_left )#line:228
    rocket_x +=rocket_vx #line:231
    rocket_y +=rocket_vy #line:232
    rocket_vy +=GRAVITY #line:233
def update_boat ():#line:239
    global boat_x ,boat_vx #line:240
    boat_x +=boat_vx #line:241
    if boat_x <WINDOW_WIDTH /2 or boat_x +BOAT_WIDTH >WINDOW_WIDTH :#line:243
        boat_vx *=-1 #line:244
def is_simulation_over ():#line:250
    if rocket_boosting ==False :#line:251
        O0OO0OO0O0O0OO00O =int (rocket_x -ROCKET_WIDTH /2 )#line:252
        O00000OOO0OO000OO =int (rocket_x +ROCKET_WIDTH /2 )#line:253
        if O0OO0OO0O0O0OO00O <0 or O00000OOO0OO000OO >=WINDOW_WIDTH :#line:256
            return True #line:257
        for O00000OOO0OO0OO0O in range (O0OO0OO0O0O0OO00O ,O00000OOO0OO000OO ):#line:260
            if (rocket_y >=WINDOW_HEIGHT -terrain_list [O00000OOO0OO0OO0O ]):#line:261
                return True #line:262
    return False #line:264
    draw_rocket ()#line:266
    draw_hud ()#line:267
def draw_terrain ():#line:273
    for O0O00OOO0OO0O0O0O in range (0 ,WINDOW_WIDTH ):#line:274
        if O0O00OOO0OO0O0O0O >GROUND_LENGTH :#line:275
            pythonGraph .draw_line (O0O00OOO0OO0O0O0O ,WINDOW_HEIGHT ,O0O00OOO0OO0O0O0O ,WINDOW_HEIGHT -terrain_list [O0O00OOO0OO0O0O0O ],"light_blue")#line:276
        else :#line:277
            pythonGraph .draw_line (O0O00OOO0OO0O0O0O ,WINDOW_HEIGHT ,O0O00OOO0OO0O0O0O ,WINDOW_HEIGHT -terrain_list [O0O00OOO0OO0O0O0O ],"green")#line:278
def draw_boat ():#line:284
    pythonGraph .draw_image ("boat.png",boat_x ,boat_y -25 ,BOAT_WIDTH ,BOAT_HEIGHT )#line:285
def draw_rocket ():#line:291
    pythonGraph .draw_image ("rocket.png",rocket_x -ROCKET_WIDTH /2 ,rocket_y -ROCKET_HEIGHT ,ROCKET_WIDTH ,ROCKET_HEIGHT )#line:292
    if rocket_thrust_up >0 :#line:293
        pythonGraph .draw_circle (rocket_x ,rocket_y ,4 ,"YELLOW",True )#line:294
    if rocket_thrust_right >0 :#line:295
        pythonGraph .draw_circle (rocket_x -ROCKET_WIDTH /3 ,rocket_y -ROCKET_HEIGHT /5 ,4 ,"YELLOW",True )#line:296
    if rocket_thrust_left >0 :#line:297
        pythonGraph .draw_circle (rocket_x +ROCKET_WIDTH /3 ,rocket_y -ROCKET_HEIGHT /5 ,4 ,"YELLOW",True )#line:298
    if rocket_y <0 :#line:299
        pythonGraph .draw_line (rocket_x -ROCKET_WIDTH /2 ,5 ,rocket_x +ROCKET_WIDTH /2 ,5 ,"YELLOW",5 )#line:300
def draw_hud ():#line:305
    pythonGraph .draw_text ("Max Score: "+str (round (max_score ,1 )),0 ,0 ,"WHITE")#line:306
    pythonGraph .draw_text ("Time Elapsed: "+str (time_elapsed ),0 ,25 ,"WHITE")#line:307
    pythonGraph .draw_text ("Fuel Consumed: "+str (round (fuel_consumed ,2 )),0 ,50 ,"WHITE")#line:308
    pythonGraph .draw_text ("X Velocity: "+str (round (rocket_vx ,2 )),0 ,75 ,"WHITE")#line:309
    pythonGraph .draw_text ("Y Velocity: "+str (round (rocket_vy ,2 )),0 ,100 ,"WHITE")#line:310
    pythonGraph .draw_text ("Crashes: "+str (num_crashes )+"  Landings: "+str (num_landings ),0 ,125 ,"WHITE")#line:311
def update_objects ():#line:316
    update_boat ()#line:317
    update_rocket ()#line:318
def update_rocket ():#line:324
    global rocket_x ,rocket_y ,rocket_vy ,rocket_vx ,rocket_boosting ,rocket_thrust_up ,rocket_thrust_right ,rocket_thrust_left ,fuel_consumed #line:325
    if rocket_boosting ==True :#line:328
        rocket_thrust_up =0 #line:330
        rocket_thrust_right =0 #line:331
        rocket_thrust_left =0 #line:332
        if rocket_y <WINDOW_HEIGHT /2 :#line:334
            rocket_thrust_right =0.25 #line:335
        else :#line:336
            rocket_thrust_up =0.35 #line:337
        if rocket_x >GROUND_LENGTH :#line:339
            rocket_boosting =False #line:340
    rocket_vy -=rocket_thrust_up #line:343
    rocket_vx -=abs (rocket_thrust_left )#line:344
    rocket_vx +=abs (rocket_thrust_right )#line:345
    fuel_consumed =fuel_consumed +abs (rocket_thrust_up )+abs (rocket_thrust_right )+abs (rocket_thrust_left )#line:348
    rocket_x +=rocket_vx #line:351
    rocket_y +=rocket_vy #line:352
    rocket_vy +=GRAVITY #line:353
def update_boat ():#line:359
    global boat_x ,boat_vx #line:360
    boat_x +=boat_vx #line:361
    if boat_x <WINDOW_WIDTH /2 or boat_x +BOAT_WIDTH >WINDOW_WIDTH :#line:363
        boat_vx *=-1 #line:364
def is_simulation_over ():#line:370
    if rocket_boosting ==False :#line:371
        O00O000000OO0OO0O =int (rocket_x -ROCKET_WIDTH /2 )#line:372
        O0O00OOO00OOOOO0O =int (rocket_x +ROCKET_WIDTH /2 )#line:373
        if O00O000000OO0OO0O <0 or O0O00OOO00OOOOO0O >=WINDOW_WIDTH :#line:376
            return True #line:377
        for OOOOOO00O00OOO0O0 in range (O00O000000OO0OO0O ,O0O00OOO00OOOOO0O ):#line:380
            if (rocket_y >=WINDOW_HEIGHT -terrain_list [OOOOOO00O00OOO0O0 ]):#line:381
                return True #line:382
    return False #line:384
