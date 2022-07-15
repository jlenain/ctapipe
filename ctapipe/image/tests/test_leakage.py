import numpy as np


def test_leakage(prod5_lst):
    from ctapipe.image.leakage import leakage_parameters

    geom = prod5_lst.camera.geometry

    img = np.ones(geom.n_pixels)
    mask = np.ones(len(geom), dtype=bool)

    l = leakage_parameters(geom, img, mask)

    ratio1 = np.sum(geom.get_border_pixel_mask(1)) / geom.n_pixels
    ratio2 = np.sum(geom.get_border_pixel_mask(2)) / geom.n_pixels

    assert l.intensity_width_1 == ratio1
    assert l.intensity_width_2 == ratio2
    assert l.pixels_width_1 == ratio1
    assert l.pixels_width_2 == ratio2
