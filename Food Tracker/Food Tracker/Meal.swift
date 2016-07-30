//
//  Meal.swift
//  Food Tracker
//
//  Created by Anthony Lee on 7/27/16.
//  Copyright © 2016 inSightFul inc. All rights reserved.
//

import UIKit

class Meal {
    
    // MARK: Properties
    var name: String
    var photo: UIImage?
    var rating: Int
    
    // MARK: Initialization
    
    init?(name: String, photo: UIImage?, rating: Int) {
        
        // Initialize stored properties
        self.name = name
        self.photo = photo
        self.rating = rating
        
        // Initialisation should fail if there is no name or rating is negative
        if name.isEmpty || rating < 0 {
            return nil
        }
    }
}
