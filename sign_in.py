import pygame
import sys

pygame.init()
save = False
username = "1"
password = "2"

width, height = 400, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sign in")

white = (255, 255, 255)
black = (0, 0, 0)
gray = (200, 200, 200)

font = pygame.font.Font(None, 36)

input_box_username = pygame.Rect(50, 100, 300, 50)
input_box_password = pygame.Rect(50, 160, 300, 50)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color_username = color_inactive
color_password = color_inactive
text_username = ''
text_password = ''
active_box = None

button_rect = pygame.Rect(50, 250, 100, 50)
button_color = gray
button_text = font.render("Sign In", True, black)
button_text_rect = button_text.get_rect(center=button_rect.center)

def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

def main_write():
    global text_username, text_password

    file_name = f"{text_username}.txt"

    write_to_file(file_name, text_password)
    print(f"user '{text_username}' created ,password set")



def draw_text(surface, text, pos, color):
    words = [word.split(' ') for word in text.splitlines()]
    space = font.size(' ')[0]
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, True, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]
                y += word_height
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]
        y += word_height

def login_screen():
    screen.fill(white)

    pygame.draw.rect(screen, color_username, input_box_username, 2)
    pygame.draw.rect(screen, color_password, input_box_password, 2)
    pygame.draw.rect(screen, gray, button_rect)

    draw_text(screen, "Username:", (50, 100), black)
    draw_text(screen, "Password:", (50, 160), black)

    txt_surface_username = font.render(text_username, True, color_username)
    txt_surface_password = font.render('*' * len(text_password), True, color_password)

    width_username = max(200, txt_surface_username.get_width() + 10)
    input_box_username.w = width_username

    width_password = max(200, txt_surface_password.get_width() + 10)
    input_box_password.w = width_password

    screen.blit(txt_surface_username, (input_box_username.x + 5, input_box_username.y + 20))
    screen.blit(txt_surface_password, (input_box_password.x + 5, input_box_password.y + 25))
    screen.blit(button_text, button_text_rect)



def main():
    clock = pygame.time.Clock()
    global text_username, text_password, active_box, color_username, color_password, button_color, save, username, password

    while True:
        save = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box_username.collidepoint(event.pos):
                    active_box = input_box_username
                    color_username = color_active
                    color_password = color_inactive
                elif input_box_password.collidepoint(event.pos):
                    active_box = input_box_password
                    color_password = color_active
                    color_username = color_inactive
                elif button_rect.collidepoint(event.pos):
                    save = True
                else:
                    active_box = None
                    color_username = color_inactive
                    color_password = color_inactive
                button_color = gray if not button_rect.collidepoint(event.pos) else white
            if event.type == pygame.KEYDOWN:
                if active_box:
                    if event.key == pygame.K_RETURN:
                        if active_box == input_box_username:
                            pass
                        elif active_box == input_box_password:
                            pass
                    elif event.key == pygame.K_BACKSPACE:
                        if active_box == input_box_username:
                            text_username = text_username[:-1]
                        elif active_box == input_box_password:
                            text_password = text_password[:-1]
                    else:
                        if active_box == input_box_username:
                            text_username += event.unicode
                        elif active_box == input_box_password:
                            text_password += event.unicode

        login_screen()
        if save == True:
            main_write()


        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
