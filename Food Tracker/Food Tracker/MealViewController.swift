//
//  ViewController.swift
//  Food Tracker
//
//  Created by Anthony Lee on 1/30/16.
//  Copyright © 2016 inSightFul inc. All rights reserved.
//

import UIKit

class MealViewController: UIViewController, UITextFieldDelegate, UIImagePickerControllerDelegate, UINavigationControllerDelegate {
    
    // MARK: Properties
    
    @IBOutlet weak var nameTextField: UITextField!
    //@IBOutlet weak var mealNameLabel: UILabel!
    @IBOutlet weak var photoImageView: UIImageView!
    @IBOutlet weak var saveButton: UIBarButtonItem!
    @IBOutlet weak var ratingControl: RatingControl!
    
    /*
     This value is either passed by `MealTableViewController` in `prepareForSegue(_:sender:)`
     or constructed as part of adding a new meal.
     */
    var meal: Meal?
    
    override func viewDidLoad() {
        
        super.viewDidLoad()
        
        // Handle the text field’s user input through delegate callbacks.
        nameTextField.delegate = self
        
        // Set up views if editing an existing Meal.
        if let meal = meal {
            navigationItem.title = meal.name
            nameTextField.text   = meal.name
            photoImageView.image = meal.photo
            ratingControl.rating = meal.rating
        }
        
        // Enable the Save button only if the text field has a valid Meal name.
        checkValidMealName()
        
    }

    override func didReceiveMemoryWarning() {
        
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    // MARK: UITextFieldDelegate
    
        func textFieldShouldReturn(textField: UITextField) -> Bool {
            
            // Hide the keyboard.
            textField.resignFirstResponder()
            return true
        }
    
        func textFieldDidEndEditing(textField: UITextField) {
            //mealNameLabel.text = textField.text
            
            // The first line calls checkValidMealName() to check if the text field has text in it, which enables the Save button if it does. 
            // The second line sets the title of the scene to that text.
            
            checkValidMealName()
            navigationItem.title = textField.text
        }
    
        func textFieldDidBeginEditing(textField: UITextField) {
            
            // Disable the Save button while editing.
            saveButton.enabled = false
        }
    
    
        func checkValidMealName() {
            
            // Disable the Save button if the text field is empty.
            let text = nameTextField.text ?? ""
            saveButton.enabled = !text.isEmpty
        }
    
    // MARK: UIImagePickerControllerDelegate
    
        func imagePickerControllerDidCancel(picker: UIImagePickerController) {
            
            // Dismiss the picker if the user canceled.
            dismissViewControllerAnimated(true, completion: nil)
        }
    
        func imagePickerController(picker: UIImagePickerController, didFinishPickingMediaWithInfo info: [String : AnyObject]) {
            
            // The info dictionary contains multiple representations of the image, and this uses the original.
            let selectedImage = info[UIImagePickerControllerOriginalImage] as! UIImage
        
            // Set photoImageView to display the selected image.
            photoImageView.image = selectedImage
        
            // Dismiss the picker.
            dismissViewControllerAnimated(true, completion: nil)
            
        }
    
    // MARK: Navigation
    
    @IBAction func cancel(sender: UIBarButtonItem) {
        
        // Depending on style of presentation (modal or push presentation), this view controller needs to be dismissed in two different ways.
        
        let isPresentingInAddMealMode = presentingViewController is UINavigationController
        
        // executes the code within the if statement only when isPresentingInAddMealMode is true
        
        if isPresentingInAddMealMode {
            
            // dismiss the meal scene without storing any information. When the meal scene gets dismissed, the meal list is shown.
            dismissViewControllerAnimated(true, completion: nil)
        }
        
        // The else clause gets executed when the meal scene was pushed onto the navigation stack on top of the meal list scene. The code within the else clause executes a method called popViewControllerAnimated, which pops the current view controller (meal scene) off the navigation stack of navigationController and performs an animation of the transition.
            
        else {
            navigationController!.popViewControllerAnimated(true)
        }
        
    }
    
    // This method lets you configure a view controller before it's presented.
    override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
        
        if saveButton === sender {
            let name = nameTextField.text ?? ""
            let photo = photoImageView.image
            let rating = ratingControl.rating
            
            // Set the meal to be passed to MealTableViewController after the unwind segue.
            meal = Meal(name: name, photo: photo, rating: rating)
        }
    }
    
    // MARK: Actions
    
    @IBAction func selectImageFromPhotoLibrary(sender: UITapGestureRecognizer) {
        
        // Hide the keyboard.
        nameTextField.resignFirstResponder()
        
        // UIImagePickerController is a view controller that lets a user pick media from their photo library.
        let imagePickerController = UIImagePickerController()
        
        // Only allow photos to be picked, not taken.
        imagePickerController.sourceType = .PhotoLibrary
        
        // Make sure ViewController is notified when the user picks an image.
        imagePickerController.delegate = self
        
        presentViewController(imagePickerController, animated: true, completion: nil)
    }
    
//        @IBAction func setDefaultLabelText(sender: UIButton) {
//        mealNameLabel.text = "Default Text"
//    }
    


}

