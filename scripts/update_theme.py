import sys

def update_colors():
    file_path = 'pages/legal/enquiry.html'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Change background of right panel to white
    content = content.replace('background: var(--navy);', 'background: #ffffff;', 1)
    
    # Update form-control border and text color
    old_fc = """            border-bottom: 2px solid rgba(255,255,255,0.15);
            padding: 10px 0;
            font-family: var(--font-body);
            font-size: 1.1rem;
            color: #fff;"""
    new_fc = """            border-bottom: 2px solid rgba(10, 17, 40, 0.15);
            padding: 10px 0;
            font-family: var(--font-body);
            font-size: 1.1rem;
            color: var(--navy);"""
    content = content.replace(old_fc, new_fc)

    # Update floating label
    old_label = """        .floating-label {
            position: absolute;
            top: 12px;
            left: 0;
            font-size: 1.1rem;
            color: rgba(255,255,255,0.4);"""
    new_label = """        .floating-label {
            position: absolute;
            top: 12px;
            left: 0;
            font-size: 1.1rem;
            color: rgba(10, 17, 40, 0.4);"""
    content = content.replace(old_label, new_label)

    # Update button disabled state
    old_btn_dis = """        .submit-btn:disabled {
            background: rgba(255,255,255,0.1);
            color: rgba(255,255,255,0.3);"""
    new_btn_dis = """        .submit-btn:disabled {
            background: #e0ddd5;
            color: #999;"""
    content = content.replace(old_btn_dis, new_btn_dis)

    # Update button hover state
    old_btn_hov = """        .submit-btn:not(:disabled):hover {
            background: #fff;"""
    new_btn_hov = """        .submit-btn:not(:disabled):hover {
            background: var(--navy);
            color: #fff;"""
    content = content.replace(old_btn_hov, new_btn_hov)

    # Update success panel
    old_sp_h2 = """        .success-panel h2 {
            font-family: var(--font-heading);
            font-size: 3rem;
            color: #fff;"""
    new_sp_h2 = """        .success-panel h2 {
            font-family: var(--font-heading);
            font-size: 3rem;
            color: var(--navy);"""
    content = content.replace(old_sp_h2, new_sp_h2)

    old_sp_p = """        .success-panel p {
            color: rgba(255,255,255,0.7);"""
    new_sp_p = """        .success-panel p {
            color: var(--muted);"""
    content = content.replace(old_sp_p, new_sp_p)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print("Success")

if __name__ == '__main__':
    update_colors()
