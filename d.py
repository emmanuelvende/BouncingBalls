import math
import pygame


def apply_rotation(theta, u):
    return (
        math.cos(theta) * u[0] - math.sin(theta) * u[1],
        math.sin(theta) * u[0] + math.cos(theta) * u[1],
    )


def draw_angled_arrow(surface, start_pos, length, angle, color, head_length=None):
    ar_len = length
    hd_len = head_length if head_length else ar_len / 5
    hd_angle = 30 * math.pi / 180
    st = start_pos
    ed = (
        st[0] + math.cos(angle) * ar_len,
        st[1] - math.sin(angle) * ar_len,
    )

    lft = ed[0] - hd_len * math.cos(hd_angle), ed[1] - hd_len * math.sin(hd_angle)
    rgt = ed[0] - hd_len * math.cos(hd_angle), ed[1] + hd_len * math.sin(hd_angle)

    lft_vec = ed[0] - lft[0], ed[1] - lft[1]
    lft_vec = apply_rotation(math.pi - angle, lft_vec)

    rgt_vec = ed[0] - rgt[0], ed[1] - rgt[1]
    rgt_vec = apply_rotation(math.pi - angle, rgt_vec)

    pygame.draw.line(surface, color, st, ed, width=2)
    pygame.draw.line(
        surface,
        color,
        ed,
        (ed[0] + lft_vec[0], ed[1] + lft_vec[1]),
        width=2,
    )
    pygame.draw.line(
        surface,
        color,
        ed,
        (ed[0] + rgt_vec[0], ed[1] + rgt_vec[1]),
        width=2,
    )
