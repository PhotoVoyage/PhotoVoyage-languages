package org.Sstudiosdev.team;

import javax.swing.*;
import java.awt.*;

public class Russian extends JFrame {
    private JList<String> wordList;

    public Russian() {
        setTitle("Русская загрузка");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new FlowLayout());

        JLabel label = new JLabel("Список слов на русском:");
        add(label);

        DefaultListModel<String> listModel = new DefaultListModel<>();
        listModel.addElement("NONE ❌");
        wordList = new JList<>(listModel);
        wordList.setLayoutOrientation(JList.VERTICAL);
        JScrollPane listScroller = new JScrollPane(wordList);
        listScroller.setPreferredSize(new Dimension(250, 80));
        add(listScroller);

        pack();
        setLocationRelativeTo(null);
        setVisible(true);
    }

    public static void main(String[] args) {
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new Russian();
            }
        });
    }
}

