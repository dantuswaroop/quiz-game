# Universal Quiz Game

A fun, interactive quiz game that tests your knowledge of flowers, fruits, country flags, and animals. The game features keyboard navigation, auto-progression, pronunciation guides, and mobile-friendly design.

## Features

### 🎮 Game Mechanics
- **Multiple Categories**: Choose from Flowers, Fruits, Country Flags, or Animals
- **Visual Learning**: High-quality images for each quiz item
- **Multiple Choice**: 4 options per question with numbered selection
- **Auto-Progression**: Questions advance automatically after 3 seconds or when spacebar is pressed
- **Scoring System**: Track your progress with real-time score updates
- **Timer**: 10-second countdown for each question

### 🎹 Controls
- **Keyboard Navigation**: Press 1-4 to select answers
- **Spacebar**: Advance to next question
- **Mouse/Touch**: Click or tap on options

### 🔊 Audio Features
- **Text-to-Speech**: Hear correct pronunciations
- **Sound Effects**: Pleasant audio feedback for correct/incorrect answers
- **Phonetic Guides**: Written pronunciation guides for difficult words

### 📱 Mobile Support
- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Touch-Friendly**: Large touch targets for mobile users
- **Orientation Support**: Adapts to portrait and landscape modes

## Getting Started

### Prerequisites
- A modern web browser (Chrome, Firefox, Safari, Edge)
- Image files organized in appropriate folders:
  - Root directory: Flower images (*.png)
  - `fruits/` folder: Fruit images
  - `flags/` folder: Country flag images
  - `animals/` folder: Animal images

### Installation
1. Download all files to a folder on your computer
2. Ensure image files are in the correct directories
3. Open `flower-game.html` in your web browser

### File Structure
```
Flower-Game/
├── flower-game.html          # Main game file
├── README.md                 # This file
├── *.png                     # Flower images (47 files)
├── fruits/
│   └── *.png                 # Fruit images (46 files)
├── flags/
│   └── *.png                 # Flag images (20 files)
└── animals/
    └── *.png                 # Animal images (20 files)
```

## How to Play

1. **Select Category**: Choose from the dropdown menu (Flowers, Fruits, Flags, Animals)
2. **View Image**: An image will appear for 3 seconds
3. **Choose Answer**: Select from 4 options using:
   - Mouse/touch: Click the correct option
   - Keyboard: Press 1, 2, 3, or 4
4. **Get Feedback**: See if you're correct and learn the pronunciation
5. **Continue**: Press spacebar or wait 3 seconds for the next question
6. **Complete Quiz**: See your final score and performance message

## Game Content

### Flowers (47 items)
Includes common and exotic flowers like roses, tulips, orchids, and more specialized varieties like frangipani and echinacea.

### Fruits (46 items)
Features fruits from around the world including tropical fruits, berries, and exotic varieties like dragon fruit and durian.

### Country Flags (20 items)
Covers major world flags including USA, UK, France, Germany, Japan, China, India, and more.

### Animals (20 items)
Includes mammals, birds, and marine life from lions and tigers to penguins and dolphins.

## Technical Features

### Browser Compatibility
- Chrome 60+
- Firefox 55+
- Safari 11+
- Edge 79+

### Performance
- Lightweight HTML/CSS/JavaScript
- No external dependencies
- Fast loading and smooth animations
- Optimized for mobile devices

### Accessibility
- Keyboard navigation support
- Screen reader friendly
- High contrast design
- Audio pronunciation guides

## Hosting Options

The game can be easily hosted on various platforms:

### GitHub Pages (Recommended)
1. Create a GitHub repository
2. Upload all files
3. Enable GitHub Pages in repository settings
4. Access via `https://yourusername.github.io/repository-name`

### Other Options
- **Netlify**: Drag and drop deployment
- **Vercel**: Connect GitHub repository for automatic deployment
- **Firebase Hosting**: Google's hosting platform
- **Surge.sh**: Simple static site deployment

## Customization

### Adding New Categories
1. Add category data to the `quizCategories` object in the JavaScript
2. Include image files in appropriate directories
3. Add phonetic pronunciations to the `phoneticMap`

### Modifying Game Settings
- **Timer Duration**: Change `timeLeft = 10` in the `startTimer()` function
- **Auto-advance Delay**: Modify the 3000ms timeout in `checkAnswer()` and `handleTimeUp()`
- **Question Display Delay**: Adjust the 3000ms timeout in `loadQuestion()`

### Styling
The game uses CSS custom properties and can be easily themed by modifying the CSS variables and color schemes.

## Development

### Code Structure
- **HTML**: Semantic structure with accessibility in mind
- **CSS**: Mobile-first responsive design with CSS Grid and Flexbox
- **JavaScript**: Modular functions with clean separation of concerns

### Key Functions
- `loadQuestion()`: Loads new quiz items
- `checkAnswer()`: Handles answer validation
- `showOptions()`: Generates multiple choice options
- `speakItemName()`: Text-to-speech functionality
- `updateTimer()`: Timer management

## Browser Support

### Audio Features
- Web Speech API for text-to-speech
- Web Audio API for sound effects
- Graceful degradation when APIs not available

### Required Permissions
- Microphone: Not required
- Camera: Not required
- Location: Not required

## Troubleshooting

### Common Issues
1. **Images not loading**: Check file paths and ensure images are in correct directories
2. **Audio not working**: Some browsers require user interaction before playing audio
3. **Speech not working**: Web Speech API availability varies by browser and system

### Performance Tips
- Ensure images are optimized (PNG format recommended)
- Use modern browsers for best performance
- Close other applications for smooth mobile experience

## License

This project is open source and available under the MIT License.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test across different browsers and devices
5. Submit a pull request

## Version History

- **v1.0**: Initial release with basic quiz functionality
- **v1.1**: Added keyboard navigation and auto-progression
- **v1.2**: Enhanced mobile compatibility and touch support
- **v1.3**: Added pronunciation guides and audio feedback

## Contact

For questions, suggestions, or bug reports, please create an issue in the project repository.

---

**Enjoy learning and testing your knowledge with the Universal Quiz Game!** 🎓✨
