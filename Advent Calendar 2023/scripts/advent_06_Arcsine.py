from advent_02_Beta import plot_beta

figure = plot_beta([(0.5, 0.5)], dpi=200, title=f"\n Arcsine Distribution", line_labels=False)
figure.savefig('06_Arcsine')
