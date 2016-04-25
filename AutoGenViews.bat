call "C:\Program Files\Python35\Lib\site-packages\PyQt4\pyuic4.bat" PlotViewer\views\MainView.ui -o PlotViewer\views\gen\ui_main_view.py

call "C:\Program Files\Python35\Lib\site-packages\PyQt4\pyuic4.bat" PlotViewer\views\MplWidget.ui -o PlotViewer\views\gen\ui_mpl_widget.py

call "C:\Program Files\Python35\Lib\site-packages\PyQt4\pyrcc4.exe" -py3 PlotViewer\views\icons.qrc -o PlotViewer\views\gen\icons_rc.py