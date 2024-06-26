package org.Sstudiosdev.team;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class MenuManager {
    public static void createMenu(JFrame parent) {
        JMenuBar menuBar = new JMenuBar();

        JMenu settingsMenu = new JMenu("Settings");
        JMenuItem exitMenuItem = new JMenuItem("Exit");
        exitMenuItem.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                parent.dispose();
            }
        });
        settingsMenu.add(exitMenuItem);
        menuBar.add(settingsMenu);

        JMenu languagesMenu = new JMenu("Languages");
        JMenuItem downloadLanguageItem = new JMenuItem("Download Language");
        downloadLanguageItem.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                showLanguageDownload(parent);
            }
        });
        languagesMenu.add(downloadLanguageItem);

        JMenuItem creditsItem = new JMenuItem("Credits");
        creditsItem.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                showCredits(parent);
            }
        });
        languagesMenu.add(creditsItem);

        menuBar.add(languagesMenu);

        parent.setJMenuBar(menuBar);
    }

    private static void showCredits(JFrame parent) {
        CreditsWindow creditsWindow = new CreditsWindow();
        creditsWindow.setVisible(true);
    }

    private static void showLanguageDownload(JFrame parent) {
        LanguageDownloadWindow languageDownloadWindow = new LanguageDownloadWindow();
        languageDownloadWindow.setVisible(true);
    }

}
