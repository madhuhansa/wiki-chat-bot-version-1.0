# wiki_summary.py
import wikipedia

def get_summary(term):
    try:
        summary = wikipedia.summary(term, sentences=3)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Too many results. Did you mean: {', '.join(e.options[:3])}?"
    except wikipedia.exceptions.PageError:
        return "No Wikipedia page found for that term."
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    while True:
        user_input = input("Enter a word or name (or 'exit' to quit): ")
        if user_input.lower() == "exit":
            break
        result = get_summary(user_input)
        print("\n" + result + "\n")

if __name__ == "__main__":
    main()
