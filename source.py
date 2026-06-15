import pygame 
#disclaimer : this button set is ai generated , got bigger fish to fry than designing a button class for 5 hours..
class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, text_color=pygame.Color('white')):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.text_color = text_color
        self.is_hovered = False
        self.clicked = False

        # Load custom font (font.ttf in your folder)
        try:
            self.font = pygame.font.Font("font.ttf", 24)
        except:
            # Fallback to default font if custom font not found
            self.font = pygame.font.Font(None, 24)
            print("Custom font not found, using default")

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.is_hovered = self.rect.collidepoint(event.pos)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.rect.collidepoint(event.pos):
                self.clicked = True
                return True

        elif event.type == pygame.MOUSEBUTTONUP:
            self.clicked = False

        return False

    def draw(self, screen):
        """Draw the button on screen"""
        # Choose color based on state
        if self.clicked:
            current_color = self.hover_color  # Darker when clicked
        elif self.is_hovered:
            current_color = self.hover_color  # Darker when hovered
        else:
            current_color = self.color

        # Draw button background with rounded corners
        pygame.draw.rect(screen, current_color, self.rect, border_radius=8)
        pygame.draw.rect(screen, pygame.Color('black'), self.rect, 2, border_radius=8)

        # Render text
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)

        # Draw text
        screen.blit(text_surface, text_rect)

    def set_position(self, x, y):
        """Move button to new position"""
        self.rect.x = x
        self.rect.y = y

    def set_text(self, new_text):
        """Change button text"""
        self.text = new_text


def process

































