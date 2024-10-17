from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioMeterInformation
import pygame
import numpy as np
import math

pygame.init()

image = pygame.image.load('img.png')
image_size = (480, 480)
image = pygame.transform.scale(image, image_size)

window_width, window_height = 800, 800
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Audio Visualizer")

center_x, center_y = window_width // 2, window_height // 2
radius = 250

background_color = (255, 255, 0)
sensitivity = 20

print("Start requested audio session...")
sessions = AudioUtilities.GetAllSessions()

print("Available audio sessions:")
for session in sessions:
    if session.Process:
        print(f"Process: {session.Process.name()}")

target_process_name = "chrome.exe"

target_session = None
for session in sessions:
    if session.Process and session.Process.name() == target_process_name:
        target_session = session
        break

if not target_session:
    raise Exception(f"{target_process_name} process not found among audio sessions")

print(f"The process session has been hijacked: {target_process_name}")

audio_meter = target_session._ctl.QueryInterface(IAudioMeterInformation)

def get_audio_volume():
    """Function to get the current volume level of an audio session"""
    peak_value = audio_meter.GetPeakValue()
    return peak_value

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    volume = get_audio_volume()

    frequency_data = np.random.rand(512) * volume * sensitivity

    screen.fill(background_color)

    image_rect = image.get_rect(center=(center_x, center_y))
    screen.blit(image, image_rect)

    buffer_length = len(frequency_data)
    spacing = 3
    angle_step = (math.pi * 2 / buffer_length) * spacing

    for i in range(buffer_length):
        bar_height = frequency_data[i] * sensitivity
        angle = i * angle_step

        x = int(center_x + math.cos(angle) * (radius + bar_height))
        y = int(center_y + math.sin(angle) * (radius + bar_height))

        r = int(abs(math.sin(angle) * 255))
        g = int(abs(math.cos(angle) * 255))
        b = 200

        pygame.draw.line(screen, (r, g, b),
                         (int(center_x + math.cos(angle) * radius), int(center_y + math.sin(angle) * radius)),
                         (x, y), 6)

    pygame.display.flip()

pygame.quit()