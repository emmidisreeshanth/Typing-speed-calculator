import time
text = "The quick brown fox jumps over the lazy dog"
print("Typing Speed Test")
print("Type the following sentence:")
print(text)
input("Press Enter when you are ready to start...")
start_time=time.time()
typed_text=input("Start typing here:")
end_time=time.time()
time_taken=end_time - start_time   
word_count=len(typed_text.split())
wpm=word_count / (time_taken / 60)
cpm=len(typed_text) / (time_taken / 60)
correct_chars=0
for i in range(min(len(typed_text), len(text))):
    if typed_text[i]==text[i]:
        correct_chars+=1
accuracy=(correct_chars / len(text)) * 100
print("===== RESULT =====")
print(f"Time Taken: {time_taken:.2f} seconds")
print(f"Words Per Minute (WPM): {wpm:.2f}")
print(f"Characters Per Minute (CPM): {cpm:.2f}")
print(f"Accuracy: {accuracy:.2f}%")

