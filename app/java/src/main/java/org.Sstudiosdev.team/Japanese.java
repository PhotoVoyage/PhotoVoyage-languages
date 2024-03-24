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

public class Japanese extends JFrame {
    private JList<String> wordList;
    private DefaultListModel<String> listModel;

    public Japanese(String folderPath) {
        setTitle("日本語ダウンロード");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new FlowLayout());

        JLabel label = new JLabel("日本語の単語リスト：");
        add(label);

        listModel = new DefaultListModel<>();
        wordList = new JList<>(listModel);
        wordList.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);
        wordList.setLayoutOrientation(JList.VERTICAL);
        JScrollPane listScroller = new JScrollPane(wordList);
        listScroller.setPreferredSize(new Dimension(250, 80));
        add(listScroller);

        JButton downloadButton = new JButton("ダウンロード");
        downloadButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                downloadSelectedWord(folderPath);
            }
        });
        add(downloadButton);

        generateWordList();

        pack();
        setLocationRelativeTo(null);
        setVisible(true);
    }

    private void generateWordList() {
        String[] words = {"admin.ejs", "search.ejs"};
        for (String word : words) {
            listModel.addElement(word);
        }
    }

    private void downloadSelectedWord(String folderPath) {
        String selectedWord = wordList.getSelectedValue();
        if (selectedWord != null) {
            String url = "https://raw.githubusercontent.com/PhotoVoyage/PhotoVoyage-languages/main/src/languages/Jp/" + selectedWord;
            try (InputStream in = new URL(url).openStream()) {
                String localPath = folderPath + "/" + selectedWord;
                FileOutputStream fos = new FileOutputStream(localPath);
                byte[] buffer = new byte[1024];
                int bytesRead;
                while ((bytesRead = in.read(buffer)) != -1) {
                    fos.write(buffer, 0, bytesRead);
                }
                fos.close();
                JOptionPane.showMessageDialog(this, "ダウンロード完了", selectedWord + " がダウンロードされました。保存先: " + localPath, JOptionPane.INFORMATION_MESSAGE);
            } catch (IOException ex) {
                JOptionPane.showMessageDialog(this, "ダウンロードエラー", selectedWord + " のダウンロードに失敗しました。", JOptionPane.ERROR_MESSAGE);
            }
        } else {
            JOptionPane.showMessageDialog(this, "ダウンロードする単語を選択してください。", "エラー", JOptionPane.WARNING_MESSAGE);
        }
    }

    public static void main(String[] args) {
        if (args.length < 1) {
            System.err.println("フォルダーパスを引数として提供する必要があります。");
            System.exit(1);
        }

        String folderPath = args[0];
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new Japanese(folderPath);
            }
        });
    }
}
