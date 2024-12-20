import pygame
import sys
import random
import math


pygame.init()


WIDTH, HEIGHT = 1400, 830
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("QuickSort Animado con Intercambio Visual Mejorado")


background_image = pygame.image.load("C:\\Users\\Usuario\\Pictures\\fondo.jpg")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))


background_image2 = pygame.image.load("C:\\Users\\Usuario\\Pictures\\fondo2.jpg")
background_image2 = pygame.transform.scale(background_image2, (WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 69, 0)
ORANGE = (255, 140, 0)
BLUE = (70, 130, 180)
LIGHT_BLUE = (173, 216, 230)
YELLOW = (255, 223, 0)
PURPLE = (138, 43, 226)
HOVER_COLOR = (100, 149, 237)


font = pygame.font.SysFont("Arial", 20, bold=True)
large_font = pygame.font.SysFont("Arial", 32, bold=True)
title_font = pygame.font.SysFont("Arial", 48, bold=True)


final_result = []


def draw_box(x, y, text, color=WHITE, width=100, height=50):
    pygame.draw.rect(screen, color, (x, y, width, height), border_radius=10)
    pygame.draw.rect(screen, BLACK, (x, y, width, height), 3, border_radius=10)
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_surface, text_rect)


def draw_info_box(x, y, text, width=300, height=50):
    pygame.draw.rect(screen, LIGHT_BLUE, (x, y, width, height), border_radius=10)
    pygame.draw.rect(screen, BLACK, (x, y, width, height), 3, border_radius=10)
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_surface, text_rect)


def draw_highlight_box(x, y, text, width=100, height=50):
    pygame.draw.rect(screen, YELLOW, (x, y, width, height), border_radius=10)
    pygame.draw.rect(screen, PURPLE, (x, y, width, height), 5, border_radius=10)
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_surface, text_rect)

def draw_direct_arrow(start_x, start_y, end_x, end_y, color=BLACK, label=""):
    
    pygame.draw.line(screen, color, (start_x, start_y), (end_x, end_y), 5)

    
    arrow_size = 15
    angle = math.atan2(end_y - start_y, end_x - start_x)
    left_wing_x = end_x - arrow_size * math.cos(angle + math.pi / 6)
    left_wing_y = end_y - arrow_size * math.sin(angle + math.pi / 6)
    right_wing_x = end_x - arrow_size * math.cos(angle - math.pi / 6)
    right_wing_y = end_y - arrow_size * math.sin(angle - math.pi / 6)
    pygame.draw.line(screen, color, (end_x, end_y), (left_wing_x, left_wing_y), 5)
    pygame.draw.line(screen, color, (end_x, end_y), (right_wing_x, right_wing_y), 5)

    
    if label:
        label_surface = font.render(label, True, color)
        label_rect = label_surface.get_rect(center=(end_x, end_y - 20))
        screen.blit(label_surface, label_rect)

def animate_jump(array, i, j, base_y, box_width, spacing):
    steps = 40  
    x_i = spacing + i * (box_width + spacing)
    x_j = spacing + j * (box_width + spacing)
    height_jump = 120  
    for step in range(steps + 1):
     
        t = step / steps
        x_pos_i = x_i + (x_j - x_i) * t
        x_pos_j = x_j + (x_i - x_j) * t
        y_offset = -height_jump * (4 * t * (1 - t))  

        screen.blit(background_image2, (0, 0))  
        draw_all_boxes(array, base_y, box_width, spacing, i, j, x_pos_i, x_pos_j, y_offset)
        
        if i != j: 
            draw_direct_arrow(x_pos_i + box_width // 2, base_y - 30, x_pos_i + box_width // 2, base_y - 70, ORANGE, "Índice")
            draw_direct_arrow(x_pos_j + box_width // 2, base_y - 30, x_pos_j + box_width // 2, base_y - 70, RED, "Pivote")
        pygame.display.update()
        pygame.time.delay(15)  

        
        pygame.event.pump()


def draw_all_boxes(array, base_y, box_width, spacing, i=-1, j=-1, x_pos_i=None, x_pos_j=None, y_offset=0):
    for k, value in enumerate(array):
        x = spacing + k * (box_width + spacing)
        y = base_y
        color = WHITE
        if k == i:
            x, y = x_pos_i, base_y + y_offset
            color = ORANGE
        elif k == j:
            x, y = x_pos_j, base_y + y_offset
            color = RED
        draw_box(x, y, str(value), color, box_width, 50)


def display_step_with_info(array, pivot_index, current_index, swap_text, comparison_result, desc, base_y, box_width, spacing):
    waiting = True
    while waiting:
        screen.blit(background_image2, (0, 0)) 

        
        draw_all_boxes(array, base_y, box_width, spacing)

    
        x_pivot = spacing + pivot_index * (box_width + spacing)
        x_current = spacing + current_index * (box_width + spacing)
        if pivot_index != current_index:  
            draw_direct_arrow(x_pivot + box_width // 2, base_y - 30, x_pivot + box_width // 2, base_y - 70, YELLOW, "Pivote")
            draw_direct_arrow(x_current + box_width // 2, base_y - 30, x_current + box_width // 2, base_y - 70, BLUE, "Índice actual")

        
        info_y = base_y + 150
        total_info_boxes = 3
        total_width_info = total_info_boxes * 300 + (total_info_boxes - 1) * spacing
        start_x_info = (WIDTH - total_width_info) // 2  
        draw_info_box(start_x_info, info_y, f"Intercambio: {swap_text}", 300, 50)
        draw_info_box(start_x_info + 300 + spacing, info_y, f"[{array[current_index]}] <= [pv] = {array[pivot_index]}", 300, 50)
        draw_info_box(start_x_info + 2 * (300 + spacing), info_y, f"Resultado: {comparison_result}", 300, 50)

    
        desc_text = large_font.render(desc, True, WHITE)
        screen.blit(desc_text, (20, 20))

        pygame.display.update()

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False


def quick_sort_visual(array):
    stack = [(0, len(array) - 1)]

    while stack:
        start, end = stack.pop()
        if start >= end:
            continue

        pivot = array[end]
        pivot_index = end
        swap_marker = start

        
        width, height = screen.get_size()
        box_width = min(width // len(array), 100)
        spacing = (width - (len(array) * box_width)) // (len(array) + 1)
        base_y = height // 2 - 100

        desc = f"Pivot seleccionado: {pivot}"
        swap_text = ""
        for current_index in range(start, end):
            comparison_result = array[current_index] <= pivot
            display_step_with_info(array, pivot_index, current_index, swap_text, comparison_result, desc, base_y, box_width, spacing)

            if comparison_result:
                swap_text = f"{array[current_index]} ⇌ {array[swap_marker]}"
                animate_jump(array, current_index, swap_marker, base_y, box_width, spacing)
                array[swap_marker], array[current_index] = array[current_index], array[swap_marker]
                swap_marker += 1
                desc = f"Intercambio realizado"

       
        swap_text = f"{array[end]} ⇌ {array[swap_marker]}"
        animate_jump(array, swap_marker, end, base_y, box_width, spacing)
        array[swap_marker], array[end] = array[end], array[swap_marker]
        desc = f"Pivote {pivot} colocado en posición final"
        display_step_with_info(array, pivot_index, -1, swap_text, True, desc, base_y, box_width, spacing)

       
        stack.append((start, swap_marker - 1))
        stack.append((swap_marker + 1, end))

    global final_result
    final_result = array[:]

    
    draw_animated_analysis_screen()


def draw_final_screen():
    screen.blit(background_image, (0, 0))  
    final_text = title_font.render("Ordenamiento Completado!", True, GREEN)
    screen.blit(final_text, (WIDTH // 2 - final_text.get_width() // 2, HEIGHT // 3))

    continue_text = large_font.render("Presiona ESPACIO para regresar al menú principal", True, WHITE)
    screen.blit(continue_text, (WIDTH // 2 - continue_text.get_width() // 2, HEIGHT // 2))

    pygame.display.update()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False


def draw_animated_analysis_screen():
    screen.blit(background_image2, (0, 0)) 
    analysis_text = title_font.render("Análisis del Ordenamiento QuickSort", True, GREEN)
    screen.blit(analysis_text, (WIDTH // 2 - analysis_text.get_width() // 2, HEIGHT // 6))

   
    partition_steps = [
        ("Elegir un pivote", "Elige un elemento como pivote para dividir la lista", 0),
        ("Mover elementos menores al pivote a la izquierda", "Los elementos menores se agrupan a la izquierda del pivote", 1),
        ("Mover elementos mayores al pivote a la derecha", "Los elementos mayores se agrupan a la derecha del pivote", 2),
        ("Repetir el proceso para las sublistas", "Continúa dividiendo cada sublista hasta que esté ordenada", 3)
    ]

    base_y = HEIGHT // 3
    box_width = 250
    spacing = 20

    for step_title, step_desc, step_index in partition_steps:
        waiting = True
        while waiting:
            screen.blit(background_image2, (0, 0))  
            screen.blit(analysis_text, (WIDTH // 2 - analysis_text.get_width() // 2, HEIGHT // 6))

            
            title_surface = large_font.render(step_title, True, YELLOW)
            desc_surface = font.render(step_desc, True, WHITE)
            screen.blit(title_surface, (WIDTH // 2 - title_surface.get_width() // 2, HEIGHT // 3))
            screen.blit(desc_surface, (WIDTH // 2 - desc_surface.get_width() // 2, HEIGHT // 3 + 50))

            
            if step_index == 0:  
                draw_highlight_box(WIDTH // 2 - box_width // 2, base_y, "Pivote", box_width)
            elif step_index == 1:  
                total_elements = 3
                total_width = total_elements * box_width + (total_elements - 1) * spacing
                start_x = (WIDTH - total_width) // 2 
                for i in range(total_elements):
                    x_pos = start_x + i * (box_width + spacing)
                    draw_box(x_pos, base_y + 100, f"Menor {i + 1}", ORANGE, box_width)
            elif step_index == 2:  
                total_elements = 3
                total_width = total_elements * box_width + (total_elements - 1) * spacing
                start_x = (WIDTH - total_width) // 2  
                for i in range(total_elements):
                    x_pos = start_x + i * (box_width + spacing)
                    draw_box(x_pos, base_y + 100, f"Mayor {i + 1}", RED, box_width)
            elif step_index == 3:  
                draw_box(WIDTH // 2 - box_width - spacing, base_y + 200, "Sublista Izquierda", BLUE, box_width)
                draw_box(WIDTH // 2 + spacing, base_y + 200, "Sublista Derecha", GREEN, box_width)

            pygame.display.update()
            pygame.time.delay(100)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        waiting = False

    
    continue_text = large_font.render("Presiona ESPACIO para regresar al menú principal", True, WHITE)
    screen.blit(continue_text, (WIDTH // 2 - continue_text.get_width() // 2, HEIGHT - 100))
    pygame.display.update()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False

    
    global menu
    menu = True


def draw_main_menu():
    screen.blit(background_image, (0, 0))  

    
    button_width, button_height = 250, 60
    button_start = pygame.Rect(WIDTH // 2 - button_width // 2, HEIGHT // 2 - 150, button_width, button_height)
    button_custom_list = pygame.Rect(WIDTH // 2 - button_width // 2, HEIGHT // 2 - 70, button_width, button_height)
    button_result = pygame.Rect(WIDTH // 2 - button_width // 2, HEIGHT // 2 + 10, button_width, button_height)
    button_quit = pygame.Rect(WIDTH // 2 - button_width // 2, HEIGHT // 2 + 90, button_width, button_height)

   
    def draw_animated_button(rect, color, text, border_color=BLACK, hover=False):
        if hover:
            color = HOVER_COLOR  
        pygame.draw.rect(screen, color, rect, border_radius=15)
        pygame.draw.rect(screen, border_color, rect, 3, border_radius=15)
        text_surface = font.render(text, True, WHITE)
        text_rect = text_surface.get_rect(center=(rect.x + rect.width // 2, rect.y + rect.height // 2))
        screen.blit(text_surface, text_rect)

    mouse_pos = pygame.mouse.get_pos()
    draw_animated_button(button_start, BLUE, "Iniciar Aleatorio", hover=button_start.collidepoint(mouse_pos))
    draw_animated_button(button_custom_list, LIGHT_BLUE, "Lista Personalizada", hover=button_custom_list.collidepoint(mouse_pos))
    draw_animated_button(button_result, LIGHT_BLUE, "Mostrar Resultado", hover=button_result.collidepoint(mouse_pos))
    draw_animated_button(button_quit, RED, "Salir", hover=button_quit.collidepoint(mouse_pos))

    pygame.display.update()
    return button_start, button_custom_list, button_result, button_quit


def input_custom_list_screen():
    input_box = pygame.Rect(WIDTH // 4, HEIGHT // 2 - 30, WIDTH // 2, 50)  
    user_text = ''
    waiting = True

    while waiting:
        screen.blit(background_image, (0, 0))
        prompt_text = smaller_font.render("Ingrese los números de la lista separados por comas:", True, WHITE)
        screen.blit(prompt_text, (WIDTH // 2 - prompt_text.get_width() // 2, HEIGHT // 2 - 80)) 

        pygame.draw.rect(screen, WHITE, input_box, border_radius=10)
        pygame.draw.rect(screen, BLACK, input_box, 3, border_radius=10)
        text_surface = smaller_font.render(user_text, True, BLACK)
        screen.blit(text_surface, (input_box.x + 10, input_box.y + 10))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waiting = False
                elif event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode

    try:
        return [int(num) for num in user_text.split(",")]
    except ValueError:
        return input_custom_list_screen()


smaller_font = pygame.font.Font(None, 28)  



def draw_result_screen():
   
    screen.blit(background_image2, (0, 0)) 
    result_text = title_font.render("Resultado del Ordenamiento", True, GREEN)
    screen.blit(result_text, (WIDTH // 2 - result_text.get_width() // 2, HEIGHT // 6))
    pygame.display.update()

    
    base_y = HEIGHT // 3
    width, height = screen.get_size()
    box_width = min(width // len(final_result), 100)
    spacing = (width - (len(final_result) * box_width)) // (len(final_result) + 1)
    for k in range(len(final_result)):
        for step in range(41):  
            t = step / 40
            y_pos = HEIGHT + (base_y - HEIGHT) * t
            screen.blit(background_image2, (0, 0))  
            screen.blit(result_text, (WIDTH // 2 - result_text.get_width() // 2, HEIGHT // 6))
            for i in range(k + 1):
                draw_box(spacing + i * (box_width + spacing), base_y, str(final_result[i]), WHITE, box_width, 50)
            draw_box(spacing + k * (box_width + spacing), y_pos, str(final_result[k]), WHITE, box_width, 50)
            pygame.display.update()
            pygame.time.delay(10)

    
    continue_text = large_font.render("Presiona ESPACIO para regresar al menú principal", True, WHITE)
    screen.blit(continue_text, (WIDTH // 2 - continue_text.get_width() // 2, HEIGHT - 100))
    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False
   
    base_y = HEIGHT // 3
    width, height = screen.get_size()
    box_width = min(width // len(final_result), 100)
    spacing = (width - (len(final_result) * box_width)) // (len(final_result) + 1)
    steps = 40
    for step in range(steps + 1):
        t = step / steps
        current_base_y = base_y + (1 - t) * height
        screen.blit(background_image2, (0, 0))  
        result_text = title_font.render("Resultado del Ordenamiento", True, GREEN)
        screen.blit(result_text, (WIDTH // 2 - result_text.get_width() // 2, HEIGHT // 6))
        draw_all_boxes(final_result, current_base_y, box_width, spacing)
        pygame.display.update()
        pygame.time.delay(10)

    
    screen.blit(background_image2, (0, 0))  
    result_text = title_font.render("Resultado del Ordenamiento", True, GREEN)
    screen.blit(result_text, (WIDTH // 2 - result_text.get_width() // 2, HEIGHT // 6))
    draw_all_boxes(final_result, base_y, box_width, spacing)
    continue_text = large_font.render("Presiona ESPACIO para regresar al menú principal", True, WHITE)
    screen.blit(continue_text, (WIDTH // 2 - continue_text.get_width() // 2, HEIGHT - 100))
    pygame.display.update()

    screen.blit(background_image2, (0, 0))  
    result_text = title_font.render("Resultado del Ordenamiento", True, GREEN)
    screen.blit(result_text, (WIDTH // 2 - result_text.get_width() // 2, HEIGHT // 6))

    base_y = HEIGHT // 3
    width, height = screen.get_size()
    box_width = min(width // len(final_result), 100)
    spacing = (width - (len(final_result) * box_width)) // (len(final_result) + 1)
    draw_all_boxes(final_result, base_y, box_width, spacing)

    continue_text = large_font.render("Presiona ESPACIO para regresar al menú principal", True, WHITE)
    screen.blit(continue_text, (WIDTH // 2 - continue_text.get_width() // 2, HEIGHT - 100))

    pygame.display.update()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False


running = True
sorting = False
menu = True
while running:
    if menu:
        button_start, button_custom_list, button_result, button_quit = draw_main_menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.VIDEORESIZE:
                WIDTH, HEIGHT = event.size
                screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
                background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))  
                background_image2 = pygame.transform.scale(background_image2, (WIDTH, HEIGHT))  
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_start.collidepoint(event.pos):
                    menu = False
                    sorting = True
                    array = [random.randint(1, 99) for _ in range(10)]  
                    quick_sort_visual(array)
                if button_custom_list.collidepoint(event.pos):
                    menu = False
                    sorting = True
                    array = input_custom_list_screen()  
                    quick_sort_visual(array)
                if button_result.collidepoint(event.pos):
                    menu = False
                    draw_result_screen()
                    menu = True
                if button_quit.collidepoint(event.pos):
                    running = False
    elif sorting:
        sorting = False
        menu = True

pygame.quit()
sys.exit()