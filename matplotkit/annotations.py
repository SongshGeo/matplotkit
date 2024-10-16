#!/usr/bin/env python 3.11.0
# -*-coding:utf-8 -*-
# @Author  : Shuang (Twist) Song
# @Contact   : SongshGeo@gmail.com
# GitHub   : https://github.com/SongshGeo
# Website: https://cv.songshgeo.com/


from matplotlib.axes import Axes


def add_diagonal_line(ax: Axes, **kwargs) -> Axes:
    """Add a 1:1 line to the plot.

    It's useful for comparing two variables in a scatter plot.

    Args:
        ax:
            The axes to add the line to.
        kwargs:
            Keyword arguments to pass to the plot function.

    Returns:
        The axes with the line added.
    """
    vals = [*ax.get_xlim(), *ax.get_ylim()]
    max_val = max(vals)
    min_val = min(vals)
    ax.plot([min_val, max_val], [min_val, max_val], **kwargs)
    return ax
