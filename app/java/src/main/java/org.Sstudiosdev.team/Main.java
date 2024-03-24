package org.Sstudiosdev.team;

import java.awt.*;
import java.awt.event.*;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.security.*;
import java.util.UUID;
import javax.swing.*;

public class Main extends JFrame {
    private static String generatedLicenseKey = null;

    public Main() {
        initUI();
    }

    private void initUI() {
        setTitle("PhotoVoyage languages");
        setSize(600, 400);
        setLocationRelativeTo(null);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BorderLayout());

        createMenu();

        JTextPane textPane = new JTextPane();
        textPane.setContentType("text/html");
        JScrollPane scrollPane = new JScrollPane(textPane);
        add(scrollPane, BorderLayout.CENTER);

        try {
            String markdownContent = loadMarkdownContent("/introduction-app.md");
            String htmlContent = markdownToHtml(markdownContent);
            textPane.setText(htmlContent);
        } catch (IOException e) {
            JOptionPane.showMessageDialog(this, "Error: " + e.getMessage(), "Error", JOptionPane.ERROR_MESSAGE);
        }

        LicenseDialog licenseDialog = new LicenseDialog(this);
        if (licenseDialog.showDialog() == JOptionPane.OK_OPTION) {
            JOptionPane.showMessageDialog(this, "License validated. Allowing access...", "Information", JOptionPane.INFORMATION_MESSAGE);
            dispose();
        }
    }

    private void createMenu() {
        JMenuBar menubar = new JMenuBar();
        JMenu fileMenu = new JMenu("File");
        JMenuItem exitMenuItem = new JMenuItem("Exit");
        exitMenuItem.addActionListener((ActionEvent event) -> {
            System.exit(0);
        });
        fileMenu.add(exitMenuItem);
        menubar.add(fileMenu);
        setJMenuBar(menubar);
    }

    private String loadMarkdownContent(String filePath) throws IOException {
        return Files.readString(Path.of(filePath));
    }

    private String markdownToHtml(String markdownContent) {
        // Convert Markdown to HTML here
        return markdownContent;
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            Main ex = new Main();
            ex.setVisible(true);
        });
    }

    private static String generateLicenseKey() {
        UUID uniqueId = UUID.randomUUID();

        MessageDigest digest;
        try {
            digest = MessageDigest.getInstance("SHA-256");
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
            return null;
        }
        byte[] hash = digest.digest(uniqueId.toString().getBytes());
        StringBuilder hexString = new StringBuilder();
        for (byte b : hash) {
            String hex = Integer.toHexString(0xff & b);
            if (hex.length() == 1) hexString.append('0');
            hexString.append(hex);
        }

        StringBuilder formattedKey = new StringBuilder();
        for (int i = 0; i < hexString.length(); i += 4) {
            formattedKey.append(hexString.substring(i, Math.min(i + 4, hexString.length()))).append("-");
        }

        return formattedKey.toString();
    }

    private static class LicenseDialog extends JDialog {
        private final JTextField licenseField;

        public LicenseDialog(JFrame parent) {
            super(parent, "Enter License", true);
            setLayout(new BorderLayout());
            setDefaultCloseOperation(DISPOSE_ON_CLOSE);
            setLocationRelativeTo(parent);

            licenseField = new JTextField();
            JButton submitButton = new JButton("Submit");
            JButton generateButton = new JButton("Generate License");

            JPanel inputPanel = new JPanel(new GridLayout(2, 1));
            inputPanel.add(new JLabel("Enter License Key:"));
            inputPanel.add(licenseField);

            JPanel buttonPanel = new JPanel(new FlowLayout(FlowLayout.CENTER));
            buttonPanel.add(submitButton);
            buttonPanel.add(generateButton);

            add(inputPanel, BorderLayout.CENTER);
            add(buttonPanel, BorderLayout.SOUTH);

            submitButton.addActionListener((ActionEvent e) -> {
                String licenseKey = licenseField.getText().trim();
                if (licenseKey.equals(generatedLicenseKey)) {
                    dispose();
                } else {
                    JOptionPane.showMessageDialog(this, "Invalid License", "Error", JOptionPane.ERROR_MESSAGE);
                }
            });

            generateButton.addActionListener((ActionEvent e) -> {
                generatedLicenseKey = generateLicenseKey();
                licenseField.setText(generatedLicenseKey);
                JOptionPane.showMessageDialog(this, "New License Generated\nRemember, licenses are for one-time use only.", "Information", JOptionPane.INFORMATION_MESSAGE);
            });

            pack();
        }

        public int showDialog() {
            setVisible(true);
            return JOptionPane.OK_OPTION;
        }
    }
}
