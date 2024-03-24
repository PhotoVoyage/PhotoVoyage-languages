package org.Sstudiosdev.team;

import java.awt.Dimension;
import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.URL;
import javax.swing.DefaultListModel;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JList;
import javax.swing.JOptionPane;
import javax.swing.JScrollPane;
import javax.swing.ListSelectionModel;

public class Spanish extends JFrame {
    private JList<String> wordList;
    private DefaultListModel<String> listModel;

    public Spanish(String folderPath) {
        setTitle("Descargar Archivos");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new FlowLayout());

        JLabel label = new JLabel("Archivos traducidos");
        add(label);

        listModel = new DefaultListModel<>();
        wordList = new JList<>(listModel);
        wordList.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);
        wordList.setLayoutOrientation(JList.VERTICAL);
        JScrollPane listScroller = new JScrollPane(wordList);
        listScroller.setPreferredSize(new Dimension(250, 80));
        add(listScroller);

        JButton downloadButton = new JButton("Descargar");
        downloadButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                downloadFile(folderPath);
            }
        });
        add(downloadButton);

        generateWordList();

        pack();
        setLocationRelativeTo(null);
        setVisible(true);
    }

    private void generateWordList() {
        String[] palabras = {"404.ejs", "error.ejs", "login.ejs"};
        for (String palabra : palabras) {
            listModel.addElement(palabra);
        }
    }

    private void downloadFile(String folderPath) {
        String selectedFileName = wordList.getSelectedValue();
        if (selectedFileName != null) {
            String url = "https://raw.githubusercontent.com/PhotoVoyage/PhotoVoyage-languages/main/src/languages/Es/" + selectedFileName;
            try (InputStream in = new URL(url).openStream()) {
                String localPath = folderPath + "/" + selectedFileName;
                FileOutputStream fos = new FileOutputStream(localPath);
                byte[] buffer = new byte[1024];
                int bytesRead;
                while ((bytesRead = in.read(buffer)) != -1) {
                    fos.write(buffer, 0, bytesRead);
                }
                fos.close();
                JOptionPane.showMessageDialog(this, "Descarga Exitosa", "Información", JOptionPane.INFORMATION_MESSAGE);
            } catch (IOException e) {
                JOptionPane.showMessageDialog(this, "Error al descargar el archivo " + selectedFileName, "Error", JOptionPane.ERROR_MESSAGE);
            }
        } else {
            JOptionPane.showMessageDialog(this, "Por favor selecciona un archivo para descargar", "Error", JOptionPane.WARNING_MESSAGE);
        }
    }

    public static void main(String[] args) {
        if (args.length < 1) {
            System.err.println("Debe proporcionar la ruta seleccionada como argumento.");
            System.exit(1);
        }

        String folderPath = args[0];
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new Spanish(folderPath);
            }
        });
    }
}

