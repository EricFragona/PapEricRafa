import pygame





def funcao_design(color,y_coord,value,draw,length, speed,score,screen,font):
    white = (255,255,255)
    black= (0,0,0)
    if draw and length <200:
        length += speed
    elif length >= 200:
        draw = False
        length = 0
        score += value
    task = pygame.draw.circle(screen,color,(30, y_coord),20,5)
    pygame.draw.rect(screen,color,[70,y_coord - 15, 200, 30])
    pygame.draw.rect(screen,black,[75,y_coord - 10,190,20])
    pygame.draw.rect(screen,color,[70, y_coord - 15,length,30])
    Value_Text = font.render(str(round(value,1)),True, white)
    screen.blit(Value_Text,(20,y_coord - 10 ))
    return task, length, draw,score


def funcao_butoes(color,x_coord,cost, owned, manager_cost,screen,font):
    white = (255,255,255)
    black= (0,0,0)
    color_button = pygame.draw.rect(screen, color,[x_coord,340,50, 30])
    color_cost = font.render(str(round(cost, 2)),True,black)
    screen.blit(color_cost,(x_coord + 6, 350))
    if not owned:
        manager_button = pygame.draw.rect(screen, color,[x_coord,405,50, 30])
        manager_text = font.render(str(round(manager_cost, 2)),True,black)
        screen.blit(manager_text,(x_coord + 6, 410))
    else:
        manager_button = pygame.draw.rect(screen, black,[x_coord, 405,50, 30])
    return color_button, manager_button




def playgame():
        
    red = (255, 0, 0)
    green = (0,255,0)
    blue = (0,0,255)
    white = (255,255,255)
    black= (0,0,0)
    purple = (127,0,255)
    orange = (255,165,0)




    #variaveis
    green_value = 1
    red_value = 2
    orange_value = 3
    white_value = 4
    purple_value = 5
    draw_green = False
    draw_red = False
    draw_orange = False
    draw_white = False
    draw_purple = False
    green_length = 0
    red_length = 0
    orange_length = 0
    white_length = 0
    purple_length = 0
    green_speed = 5
    red_speed = 4
    orange_speed = 3
    white_speed = 2
    purple_speed = 1
    score = 0


    #funcao butoes variaveis
    green_cost = 1
    green_owned = False
    green_manager_cost = 100
    red_cost = 2
    red_owned = False
    red_manager_cost = 500
    orange_cost = 3
    orange_owned = False
    orange_manager_cost = 1800
    white_cost = 4
    white_owned = False
    white_manager_cost = 4000
    purple_cost = 5
    purple_owned = False
    purple_manager_cost = 10000

        
    
    
    
    
    pygame.init()

    screen = pygame.display.set_mode([300, 450])
    pygame.display.set_caption("No Name Game")
    background = black
    framerate = 60
    font = pygame.font.Font('freesansbold.ttf', 16)
    timer = pygame.time.Clock()

    running = True
    while running:
        timer.tick(framerate)
        if green_owned and not draw_green:
            draw_green = True
        if red_owned and not draw_red:
            draw_red = True
        if orange_owned and not draw_orange:
            draw_orange = True
        if white_owned and not draw_white:
            draw_white = True
        if purple_owned and not draw_purple:
            draw_purple = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if task1.collidepoint(event.pos):
                    draw_green = True
                if task2.collidepoint(event.pos):
                    draw_red = True
                if task3.collidepoint(event.pos):
                    draw_orange = True
                if task4.collidepoint(event.pos):
                    draw_white = True
                if task5.collidepoint(event.pos):
                    draw_purple = True
                if green_manager_buy.collidepoint(event.pos) and score >= green_manager_cost and not green_owned:
                    green_owned = True
                    score -= green_manager_cost
                if red_manager_buy.collidepoint(event.pos) and score >= red_manager_cost and not red_owned:
                    red_owned = True
                    score -= red_manager_cost
                if orange_manager_buy.collidepoint(event.pos) and score >= orange_manager_cost and not orange_owned:
                    orange_owned = True
                    score -= orange_manager_cost
                if white_manager_buy.collidepoint(event.pos) and score >= white_manager_cost and not white_owned:
                    white_owned = True
                    score -= white_manager_cost
                if purple_manager_buy.collidepoint(event.pos) and score >= purple_manager_cost and not purple_owned:
                    purple_owned = True
                    score -= purple_manager_cost
                if green_buy.collidepoint(event.pos) and score >= green_cost:
                    green_value += .15
                    score -= green_cost
                    green_cost += .1
                if red_buy.collidepoint(event.pos) and score >= red_cost:
                    red_value += .15
                    score -= red_cost
                    red_cost += .1
                if orange_buy.collidepoint(event.pos) and score >= orange_cost:
                    orange_value += .15
                    score -= orange_cost
                    orange_cost += .1
                if white_buy.collidepoint(event.pos) and score >= white_cost:
                    white_value += .15
                    score -= white_cost
                    white_cost += .1

                if purple_buy.collidepoint(event.pos) and score >= purple_cost:
                    purple_value += .15
                    score -= purple_cost
                    purple_cost += .1

        screen.fill(background)
        task1, green_length, draw_green,score = funcao_design(green, 50, green_value, draw_green, green_length, green_speed,score,screen,font)
        task2, red_length, draw_red,score = funcao_design(red, 100, red_value, draw_red, red_length, red_speed,score,screen,font)
        task3, orange_length, draw_orange,score = funcao_design(orange, 150, orange_value, draw_orange, orange_length, orange_speed,score,screen,font)
        task4, white_length, draw_white,score = funcao_design(white, 200, white_value, draw_white, white_length, white_speed,score,screen,font)
        task5, purple_length, draw_purple,score = funcao_design(purple, 250, purple_value, draw_purple, purple_length,purple_speed,score,screen,font)
        green_buy, green_manager_buy = funcao_butoes(green, 10, green_cost, green_owned, green_manager_cost,screen,font)
        red_buy, red_manager_buy = funcao_butoes(red, 70, red_cost, red_owned, red_manager_cost,screen,font)
        orange_buy, orange_manager_buy = funcao_butoes(orange, 130, orange_cost, orange_owned, orange_manager_cost,screen,font)
        white_buy, white_manager_buy = funcao_butoes(white, 190, white_cost, white_owned, white_manager_cost,screen,font)
        purple_buy, purple_manager_buy = funcao_butoes(purple, 250, purple_cost, purple_owned, purple_manager_cost,screen,font)
        display_score = font.render('Money: $' + str(round(score, 2)), True, white, black)
        screen.blit(display_score, (10, 5))
        buy_more = font.render('Buy More:', True, white)
        screen.blit(buy_more, (10, 315))
        buy_managers = font.render('Buy Managers:', True, white)
        screen.blit(buy_managers, (10, 380))
        pygame.display.flip()
    pygame.quit()
