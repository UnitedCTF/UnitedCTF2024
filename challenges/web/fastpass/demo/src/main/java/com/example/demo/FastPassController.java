package com.example.demo;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.view.RedirectView;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
public class FastPassController {

    @GetMapping("/")
    public String index() {
        return "Welcome to the fastpass API. To see available fastpasses, try /fastpasses. You can check the server state with /health.<br>" +
                "Bienvenue à l'API fastpass. Pour voir les fastpass disponibles aujourd'hui, essayez /fastpasses. L'état du serveur peut être consulté avec /health.<br>";
    }

    @GetMapping("/health")
    public RedirectView health(){
        return new RedirectView("/actuator/health");
    }

    @GetMapping("/fastpasses")
    public String fastpasses() {
        String filePath = "available_fastpasses.csv"; // Replace with your file path
        try {
            String content = new String(Files.readAllBytes(Paths.get(filePath)));
            if (content.isEmpty()) {
                return "The are no available fastpasses today. Il n'y a pas de fastpass disponible aujourd'hui.";
            } else {
                return content;
            }
        } catch (IOException e) {
            e.printStackTrace();
            return "Error reading file";
        }
    }

}