package controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;

import java.util.logging.Logger;

@Controller
public class MainController {

    @GetMapping("/greeting")
    public String greeting(@RequestParam(name="username", required=false, defaultValue="") String name,
                           @RequestParam(name="password", required = false, defaultValue = "") String pass,
                           Model model) {
        model.addAttribute("name", name);
        model.addAttribute("pass", pass);

        System.out.println("----------------");
        System.out.println("username: " + name + "\tpassord: " + pass);
        System.out.println("-----------------");

        return "greeting";
    }

//    @GetMapping
//    @RequestMapping(value = "/spy", method = RequestMethod.POST)
//    public String getPassword(@RequestBody Job job){
//        System.out.println(job);
//        return jobRepository.saveAndFlush(job);
//    }

}
