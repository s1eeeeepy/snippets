{% if messages %}
  {% for message in messages %}
    <div class="alert alert--{{ message.tags }}">
      <p class="alert__message">{{ message }}</p>
    </div>
  {% endfor %}
{% endif %}
