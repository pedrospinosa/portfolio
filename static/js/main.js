// Mobile Navigation Toggle
const hamburger = document.querySelector('.hamburger');
const navMenu = document.querySelector('.nav-menu');
const body = document.body;

// Toggle mobile menu
function toggleMobileMenu() {
    hamburger.classList.toggle('active');
    navMenu.classList.toggle('active');
    
    // Prevent body scroll when menu is open
    if (navMenu.classList.contains('active')) {
        body.style.overflow = 'hidden';
    } else {
        body.style.overflow = '';
    }
}

// Close mobile menu
function closeMobileMenu() {
    hamburger.classList.remove('active');
    navMenu.classList.remove('active');
    body.style.overflow = '';
}

// Event listeners for mobile navigation
if (hamburger) {
    hamburger.addEventListener('click', toggleMobileMenu);
}

// Close mobile menu when clicking on a link
document.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', closeMobileMenu);
});

// Close mobile menu when clicking outside
document.addEventListener('click', (e) => {
    if (!hamburger.contains(e.target) && !navMenu.contains(e.target)) {
        closeMobileMenu();
    }
});

// Close mobile menu on escape key
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && navMenu.classList.contains('active')) {
        closeMobileMenu();
    }
});

// Handle window resize
window.addEventListener('resize', () => {
    if (window.innerWidth > 768) {
        closeMobileMenu();
    }
});

// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            const navbarHeight = document.querySelector('.navbar').offsetHeight;
            const targetPosition = target.offsetTop - navbarHeight - 20;
            
            window.scrollTo({
                top: targetPosition,
                behavior: 'smooth'
            });
        }
    });
});

// Enhanced navbar background on scroll
let isScrolling = false;
function updateNavbar() {
    const navbar = document.querySelector('.navbar');
    const scrollY = window.scrollY;
    
    if (scrollY > 100) {
        navbar.style.background = 'rgba(255, 255, 255, 0.98)';
        navbar.style.boxShadow = '0 2px 10px rgba(0, 0, 0, 0.1)';
    } else {
        navbar.style.background = 'rgba(255, 255, 255, 0.95)';
        navbar.style.boxShadow = 'none';
    }
    
    isScrolling = false;
}

window.addEventListener('scroll', () => {
    if (!isScrolling) {
        requestAnimationFrame(updateNavbar);
        isScrolling = true;
    }
});

// Enhanced active navigation link highlighting
let isHighlighting = false;
function updateActiveNavigation() {
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.nav-link');
    const scrollY = window.scrollY;
    const windowHeight = window.innerHeight;
    
    let current = '';
    
    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;
        const sectionBottom = sectionTop + sectionHeight;
        
        // Check if section is in viewport
        if (scrollY >= (sectionTop - windowHeight / 3) && scrollY < (sectionBottom - windowHeight / 3)) {
            current = section.getAttribute('id');
        }
    });

    navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === `#${current}`) {
            link.classList.add('active');
        }
    });
    
    isHighlighting = false;
}

window.addEventListener('scroll', () => {
    if (!isHighlighting) {
        requestAnimationFrame(updateActiveNavigation);
        isHighlighting = true;
    }
});

// Enhanced contact form handling
const contactForm = document.getElementById('contactForm');
if (contactForm) {
    contactForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const submitBtn = this.querySelector('.btn-primary');
        const originalText = submitBtn.textContent;
        
        // Show loading state
        submitBtn.textContent = 'Sending...';
        submitBtn.disabled = true;
        
        const formData = new FormData(this);
        const name = formData.get('name').trim();
        const email = formData.get('email').trim();
        const message = formData.get('message').trim();
        
        // Enhanced validation
        if (!name || !email || !message) {
            showFormMessage('Please fill in all fields', 'error');
            resetSubmitButton();
            return;
        }
        
        if (name.length < 2) {
            showFormMessage('Name must be at least 2 characters long', 'error');
            resetSubmitButton();
            return;
        }
        
        // Enhanced email validation
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email)) {
            showFormMessage('Please enter a valid email address', 'error');
            resetSubmitButton();
            return;
        }
        
        if (message.length < 10) {
            showFormMessage('Message must be at least 10 characters long', 'error');
            resetSubmitButton();
            return;
        }
        
        // Simulate form submission delay
        setTimeout(() => {
            showFormMessage('Thank you for your message! I\'ll get back to you soon.', 'success');
            this.reset();
            resetSubmitButton();
        }, 1500);
        
        function resetSubmitButton() {
            submitBtn.textContent = originalText;
            submitBtn.disabled = false;
        }
    });
}

// Form message display function
function showFormMessage(message, type) {
    // Remove existing message
    const existingMessage = document.querySelector('.form-message');
    if (existingMessage) {
        existingMessage.remove();
    }
    
    // Create new message element
    const messageEl = document.createElement('div');
    messageEl.className = `form-message form-message-${type}`;
    messageEl.style.cssText = `
        padding: 1rem;
        margin-top: 1rem;
        border-radius: 8px;
        font-weight: 500;
        text-align: center;
        animation: fadeInUp 0.3s ease;
        ${type === 'success' ? 
            'background: #dcfce7; color: #166534; border: 1px solid #bbf7d0;' : 
            'background: #fef2f2; color: #dc2626; border: 1px solid #fecaca;'
        }
    `;
    messageEl.textContent = message;
    
    // Insert message after form
    contactForm.appendChild(messageEl);
    
    // Auto-remove message after 5 seconds
    setTimeout(() => {
        if (messageEl.parentNode) {
            messageEl.style.animation = 'fadeOutDown 0.3s ease';
            setTimeout(() => messageEl.remove(), 300);
        }
    }, 5000);
}

// Enhanced Intersection Observer for animations
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
            
            // Add staggered animation for child elements
            const children = entry.target.querySelectorAll('.skill-tag, .timeline-achievements li');
            children.forEach((child, index) => {
                setTimeout(() => {
                    child.style.opacity = '1';
                    child.style.transform = 'translateY(0)';
                }, index * 100);
            });
        }
    });
}, observerOptions);

// Initialize animations on DOM content loaded
document.addEventListener('DOMContentLoaded', () => {
    // Observe elements for animation
    const animatedElements = document.querySelectorAll(
        '.timeline-item, .skill-category, .education-card, .certification-card, .contact-item'
    );
    
    animatedElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });
    
    // Initialize skill tags for staggered animation
    const skillTags = document.querySelectorAll('.skill-tag');
    skillTags.forEach(tag => {
        tag.style.opacity = '0';
        tag.style.transform = 'translateY(10px)';
        tag.style.transition = 'opacity 0.3s ease, transform 0.3s ease';
    });
    
    // Initialize timeline achievements for staggered animation
    const achievements = document.querySelectorAll('.timeline-achievements li');
    achievements.forEach(achievement => {
        achievement.style.opacity = '0';
        achievement.style.transform = 'translateY(10px)';
        achievement.style.transition = 'opacity 0.3s ease, transform 0.3s ease';
    });
});

// Enhanced typing effect for hero title
function typeWriter(element, text, speed = 100) {
    let i = 0;
    element.innerHTML = '';
    
    function type() {
        if (i < text.length) {
            element.innerHTML += text.charAt(i);
            i++;
            setTimeout(type, speed);
        } else {
            // Add blinking cursor effect after typing is complete
            element.innerHTML += '<span class="cursor">|</span>';
            setTimeout(() => {
                const cursor = element.querySelector('.cursor');
                if (cursor) cursor.remove();
            }, 3000);
        }
    }
    
    type();
}

// Initialize typing effect when page loads
document.addEventListener('DOMContentLoaded', () => {
    const heroTitle = document.querySelector('.hero-title');
    if (heroTitle) {
        const originalText = heroTitle.textContent;
        // Add CSS for cursor animation
        const style = document.createElement('style');
        style.textContent = `
            .cursor {
                animation: blink 1s infinite;
            }
            @keyframes blink {
                0%, 50% { opacity: 1; }
                51%, 100% { opacity: 0; }
            }
        `;
        document.head.appendChild(style);
        
        typeWriter(heroTitle, originalText, 150);
    }
});

// Enhanced hover effects with touch support
function addEnhancedHoverEffects() {
    // Skill tags enhanced hover effect
    document.querySelectorAll('.skill-tag').forEach(tag => {
        tag.addEventListener('mouseenter', function() {
            this.style.transform = 'scale(1.05)';
            this.style.transition = 'transform 0.2s ease';
        });
        
        tag.addEventListener('mouseleave', function() {
            this.style.transform = 'scale(1)';
        });
        
        // Touch support for mobile
        tag.addEventListener('touchstart', function() {
            this.style.transform = 'scale(1.05)';
        });
        
        tag.addEventListener('touchend', function() {
            setTimeout(() => {
                this.style.transform = 'scale(1)';
            }, 150);
        });
    });

    // Timeline item enhanced hover effects
    document.querySelectorAll('.timeline-content').forEach(item => {
        item.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-5px)';
            this.style.boxShadow = '0 8px 25px rgba(0, 0, 0, 0.1)';
            this.style.transition = 'transform 0.3s ease, box-shadow 0.3s ease';
        });
        
        item.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
            this.style.boxShadow = '0 4px 6px rgba(0, 0, 0, 0.05)';
        });
    });
}

// Improved loading animation with performance optimization
window.addEventListener('load', () => {
    // Remove any loading indicators
    const loader = document.querySelector('.loader');
    if (loader) {
        loader.style.opacity = '0';
        setTimeout(() => loader.remove(), 500);
    }
    
    // Fade in body content
    document.body.style.opacity = '0';
    document.body.style.transition = 'opacity 0.5s ease';
    
    // Use requestAnimationFrame for smooth animation
    requestAnimationFrame(() => {
        document.body.style.opacity = '1';
    });
    
    // Initialize enhanced hover effects after load
    addEnhancedHoverEffects();
});

// Performance optimization: Debounce scroll events
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Optimize scroll performance for mobile devices
if (window.DeviceMotionEvent) {
    window.addEventListener('scroll', debounce(updateNavbar, 10));
    window.addEventListener('scroll', debounce(updateActiveNavigation, 10));
}

// Touch gesture support for mobile navigation
let touchStartX = 0;
let touchEndX = 0;

document.addEventListener('touchstart', (e) => {
    touchStartX = e.changedTouches[0].screenX;
});

document.addEventListener('touchend', (e) => {
    touchEndX = e.changedTouches[0].screenX;
    handleSwipeGesture();
});

function handleSwipeGesture() {
    const swipeThreshold = 100;
    const swipeDistance = touchEndX - touchStartX;
    
    // Swipe right to open menu (only when menu is closed and swipe starts from edge)
    if (swipeDistance > swipeThreshold && touchStartX < 50 && !navMenu.classList.contains('active')) {
        toggleMobileMenu();
    }
    
    // Swipe left to close menu
    if (swipeDistance < -swipeThreshold && navMenu.classList.contains('active')) {
        closeMobileMenu();
    }
}

// Accessibility improvements
document.addEventListener('DOMContentLoaded', () => {
    // Add ARIA labels for better accessibility
    if (hamburger) {
        hamburger.setAttribute('aria-label', 'Toggle navigation menu');
        hamburger.setAttribute('aria-expanded', 'false');
    }
    
    // Update ARIA attributes when menu toggles
    const originalToggle = toggleMobileMenu;
    toggleMobileMenu = function() {
        originalToggle();
        if (hamburger) {
            const isActive = navMenu.classList.contains('active');
            hamburger.setAttribute('aria-expanded', isActive);
        }
    };
});

// Add CSS for additional animations
const additionalStyles = document.createElement('style');
additionalStyles.textContent = `
    @keyframes fadeOutDown {
        from {
            opacity: 1;
            transform: translateY(0);
        }
        to {
            opacity: 0;
            transform: translateY(20px);
        }
    }
    
    .nav-menu {
        will-change: transform;
    }
    
    @media (prefers-reduced-motion: reduce) {
        .nav-menu {
            transition: none !important;
        }
    }
`;
document.head.appendChild(additionalStyles); 