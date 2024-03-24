package org.Sstudiosdev.team;

import javax.swing.*;
import javax.swing.filechooser.FileSystemView;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;
import java.io.IOException;

public class LanguageDownloadWindow extends JFrame {
    private JComboBox<String> languageSelector;
    private JButton selectFolderButton;
    private JButton downloadButton;
    private JLabel selectedFolderLabel;

    public LanguageDownloadWindow() {
        setTitle("Download Language");
        setBounds(100, 100, 400, 200);

        JPanel panel = new JPanel();
        panel.setLayout(new BorderLayout());

        JPanel centerPanel = new JPanel(new GridLayout(4, 1, 5, 5));
        languageSelector = new JComboBox<>();
        languageSelector.addItem("Spanish");
        languageSelector.addItem("Japanese");
        languageSelector.addItem("Russian");
        centerPanel.add(new JLabel("Select language to download:"));
        centerPanel.add(languageSelector);

        JPanel folderPanel = new JPanel(new FlowLayout(FlowLayout.LEFT));
        selectedFolderLabel = new JLabel("Selected folder: ");
        folderPanel.add(selectedFolderLabel);
        centerPanel.add(folderPanel);

        JPanel buttonPanel = new JPanel(new FlowLayout(FlowLayout.CENTER, 10, 10));
        selectFolderButton = new JButton("Select Folder");
        selectFolderButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                showFileDialog();
            }
        });
        buttonPanel.add(selectFolderButton);

        downloadButton = new JButton("Download");
        downloadButton.setEnabled(false);
        downloadButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                downloadLanguage();
            }
        });
        buttonPanel.add(downloadButton);
        centerPanel.add(buttonPanel);

        panel.add(centerPanel, BorderLayout.CENTER);
        add(panel);

        setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        setVisible(true);
    }

    private void showFileDialog() {
        JFileChooser fileChooser = new JFileChooser(FileSystemView.getFileSystemView().getDefaultDirectory());
        fileChooser.setDialogTitle("Select Directory");
        fileChooser.setFileSelectionMode(JFileChooser.DIRECTORIES_ONLY);
        int returnValue = fileChooser.showDialog(this, "Select");
        if (returnValue == JFileChooser.APPROVE_OPTION) {
            File selectedFile = fileChooser.getSelectedFile();
            String selectedFolder = selectedFile.getAbsolutePath();
            selectedFolderLabel.setText("Selected folder: " + selectedFolder);
            downloadButton.setEnabled(true);
        }
    }

    private void downloadLanguage() {
        String selectedLanguage = (String) languageSelector.getSelectedItem();
        String scriptName = "";
        if (selectedLanguage.equals("Spanish")) {
            scriptName = "Spanish-gen.py";
        } else if (selectedLanguage.equals("Japanese")) {
            scriptName = "Japanese-gen.py";
        } else if (selectedLanguage.equals("Russian")) {
            scriptName = "Russian-gen.py";
        }

        String scriptPath = "download" + File.separator + scriptName;
        File scriptFile = new File(scriptPath);
        if (scriptFile.exists()) {
            try {
                Runtime.getRuntime().exec("python " + scriptPath + " " + selectedFolderLabel.getText());
            } catch (IOException e) {
                e.printStackTrace();
            }
        } else {
            JOptionPane.showMessageDialog(this, "The script file " + scriptName + " was not found.", "File Not Found", JOptionPane.WARNING_MESSAGE);
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(LanguageDownloadWindow::new);
    }
}
